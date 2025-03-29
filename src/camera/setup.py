from setuptools import find_packages, setup

package_name = 'camera'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sudohex',
    maintainer_email='ppk1996kyaw@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_publisher = camera.hello_publisher:main',
            'maybe_pub = camera.maybe_pub:main',
        ],
    },
)
