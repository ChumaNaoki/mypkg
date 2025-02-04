from setuptools import setup
import os
from glob import glob

package_name = 'montecarlo_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name),glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Chuma Naoki',
    maintainer_email='s23C1091UY@s.chibakoudai.jp',
    description='ロボットシステム学練習用',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'monte_carlo_publisher = montecarlo_ros2.monte_carlo_publisher:main',
        'result= montecarlo_ros2.result:main',
        ],
    },
)
