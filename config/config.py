# from dynaconf import Dynaconf
#
# settings = Dynaconf(
#     envvar_prefix="DYNACONF",
#     settings_files=['./config/settings.toml', './config/secrets.toml'],
# )


from setuptools import setup, find_packages

setup(
    name='gaji-gesa-test-utils',
    version='0.1.0',
    packages=find_packages(include=['gaji-gesa-api-python-utils', 'gaji_gesa_api_python_utils.*'])
)