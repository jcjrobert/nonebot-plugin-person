import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as f:
    long_description = f.read()
    setuptools.setup(
        name='nonebot-plugin-person',
        version='0.0.2',
        author='jcjrobert',
        author_email='jcjrobbie@gmail.com',
        keywords=["pip", "nonebot2", "nonebot", "随个人"],
        url='https://github.com/jcjrobert/nonebot-plugin-person',
        description='Nonebot2 简易插件随个人，随个群友当幸运观众🤪',
        long_description=long_description,
        long_description_content_type="text/markdown",
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
        ],
        license='MIT License',
        packages=setuptools.find_packages(),
        include_package_data=True,
        platforms="any",
        install_requires=[
            'nonebot2>=2.0.0-beta.4', 'nonebot-adapter-onebot>=2.0.0-beta.4'
        ]
    )