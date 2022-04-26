import shutil
from os import getcwd, chdir

from behave.__main__ import main as behave_main
from dynaconf import settings

if __name__ == '__main__':

    if not getcwd().endswith('test-api-automation'):
        chdir('./gaji-gesa-test-api-automation')
    shutil.rmtree("allure_results", ignore_errors=True)
    settings.load_file(path="./config/settings.toml")
    behave_main(
        [
            './tests',
            '--no-logcapture',
            '-f=allure_behave.formatter:AllureFormatter',
            '-o=allure_results',
            '--tags=jaycee'
        ]
    )
