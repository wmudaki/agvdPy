#!/usr/bin/env python3
"""
The module implements a wrapper around the AGVD
Web REST services that allows one to query the
African genome variation database

"""
import requests


class Agvd:
    def signup(self, **kwargs):
        """
        Allowed Keyword Arguments

            name:
                A user's Full Name
                Example:
                    John Doe

            id:
                A unique username that will be used as a user-id when login in

                Example:
                    JDoe

            email:
                A User's email

                Example:
                    john.doe@email.com

            password:
                A Users Password; Must contain at least 8 characters, mixed-case
                characters, a numerical character and a special character

            organization:
                An organization to which a user is affiliated to

                Example:
                    H3ABionet

        :return:
        """
        return self.request('signup', kwargs)

    def login(self, **kwargs):
        """
        Allowed Keyword Arguments
            user:
                Unique user-id
            password:
                User's password

        :return:
        """

        return self.request('login', kwargs)

    def query(self, **kwargs):
        """
        Allowed Keyword arguments

            token:
                A token supplied after user login; If user doesn't want
                to log in first before making the query, the user can append their
                user-id and password as keyword parameters in the query function

            user:
                unique user-id

            password:
                user password

            id:
                List of IDs, these can be rs IDs (dbSNP)
                or variants in the format chrom:start:ref:alt

                Example:
                    rs116600158
                    COSM6350960
                    19:7177679:C:T
            region:
                List of regions, these can be just a single
                chromosome name or regions in the format
                <chromosome>:<start>-<end>

                Example:
                    chr22
                    3:100000-200000

            type:
                List of types, accepted values are SNV,
                MNV, INDEL, SV, CNV, INSERTION, DELETION

                Example:
                    SNV,INDEL

            gene:
                List of genes, most gene IDs are accepted (HGNC, Ensembl gene, ...).

                Example:
                    BRCA2
                    BMPR
                    ENSG00000174173
                    ENST00000495642

            sample:
                Filter variants where the samples contain the variant
                (HET or HOM_ALT). Accepts AND ( ; ) and OR ( , ) operators.

                Example:
                    HG0097,HG00978

            cohort:
                Select variants with calculated stats for the selected cohorts

            cohortStatsRef:
                Reference Allele Frequency: {cohort}[<|>|<=|>=]{number}.

                Example:
                    ALL>0.6

            cohortStatsAlt:
                Alternate Allele Frequency: {cohort}[<|>|<=|>=]{number}.

                Example:
                    ALL<=4

            cohortStatsMaf:
                Minor Allele Frequency: {cohort}[<|>|<=|>=]{number}.

                Example:
                    ALL<0.01

            cohortStatsMgf:
                Minor Genotype Frequency: {cohort}[<|>|<=|>=]{number}.

                Example:
                    COH1<0.1,COH2<0.3


            clinicalSignificance:
                Clinical significance: benign, likely_benign, likely_pathogenic, pathogenic

        """
        return self.request('variant', kwargs)

    @staticmethod
    def request(endpoint, params):
        handle = requests.post(f'http://localhost:3000/agvd/{endpoint}', data=params)
        return handle.json()


if __name__ == '__main__':
    pass



