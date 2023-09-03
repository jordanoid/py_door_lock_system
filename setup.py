import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'py_door_lock_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        # (os.path.join('share', package_name), glob('launch/*_launch.xml'))
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lab-embedded',
    maintainer_email='lab-embedded@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'qr_decoder = py_door_lock_system.qr_decoder_node:main',
            'lock_service = py_door_lock_system.lock_service_node:main',
            'authenticator = py_door_lock_system.api_auth_node:main',
        ],
    },
)
