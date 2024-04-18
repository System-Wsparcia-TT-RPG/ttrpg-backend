from tomllib import load

from setuptools import setup, find_packages


def main() -> None:
    with open('./pyproject.toml', 'rb') as toml_file:
        project_data: dict = load(toml_file)

    authors: str = ', '.join(map(lambda x: x['name'], project_data['project']['authors']))
    emails: str = ', '.join(map(lambda x: x['email'], project_data['project']['authors']))

    setup(
        name=project_data['project']['name'],
        description=project_data['project']['description'],
        url=project_data['project']['urls']['Homepage'],

        license='',
        version=project_data['project']['version'],

        author=authors,
        author_email=emails,

        packages=find_packages(where='src'),
        package_dir={"": "src"},
        include_package_data=True,
        package_data={"": ['**/*.html']},
    )


if __name__ == '__main__':
    main()
