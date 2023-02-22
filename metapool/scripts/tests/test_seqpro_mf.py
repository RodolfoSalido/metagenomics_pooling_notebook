import os
import unittest

import pandas as pd
from click.testing import CliRunner
from metapool.scripts.seqpro_mf import format_preparation_files_mf
from shutil import copy, copytree, rmtree
from os.path import join, exists
import re


class SeqproAmpliconTests(unittest.TestCase):
    def setUp(self):
        # we need to get the test data directory in the parent directory
        # important to use abspath because we use CliRunner.isolated_filesystem
        tests_dir = os.path.abspath(os.path.dirname(__file__))
        tests_dir = os.path.dirname(os.path.dirname(tests_dir))
        self.data_dir = os.path.join(tests_dir, 'tests', 'data')

        self.fastp_run = os.path.join(self.data_dir, 'runs',
                                      '230207_M05314_0346_000000000-KVMGL')
        self.fastp_sheet = os.path.join(self.fastp_run,
                                        'sample_mapping_file.tsv')

        # before continuing, create a copy of
        # 230207_M05314_0346_000000000-KVMGL and replace Stats sub-dir with
        # Reports.
        self.temp_copy = self.fastp_run.replace('230207', '240207')
        copytree(self.fastp_run, self.temp_copy)
        rmtree(join(self.temp_copy, 'Stats'))
        os.makedirs(join(self.temp_copy, 'Reports'))
        copy(join(self.data_dir, 'Demultiplex_Stats.csv'),
             join(self.temp_copy, 'Reports', 'Demultiplex_Stats.csv'))

    def test_run(self):
        runner = CliRunner()

        with runner.isolated_filesystem():
            result = runner.invoke(format_preparation_files_mf,
                                   args=[self.temp_copy,
                                         join(self.temp_copy,
                                              'sample_mapping_file.tsv'),
                                         './'])

            # assert seqpro_mf returned successfully
            self.assertEqual(result.exit_code, 0)

            exp_fp = ('./240207_M05314_0346_000000000-KVMGL.ABTX_20230208_'
                      'ABTX_11052.1.tsv')

            # assert prep-info-file output exists
            self.assertTrue(exists(exp_fp))

            # assert sample_name does not contain any '_' characters
            names = list(pd.read_csv(exp_fp, delimiter='\t')['sample_name'])

            # generate a list of sample-names that contain characters other
            # than alphanumerics + '.'
            names = [x for x in names if not bool(re.match(r"^[\w\d.]*$", x))]

            # assert that all sample-names were of the proper form.
            self.assertEqual(names, [])

    def tearDown(self):
        rmtree(self.temp_copy)


if __name__ == '__main__':
    unittest.main()
