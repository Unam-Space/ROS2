from setuptools import setup

package_name = 'rover_gui'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lolineko',
    maintainer_email='317292181@pcpuma.acatlan.unam.mx',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talkerNode = rover_gui.talker:main',
            #'listenerNode = rover_gui.listener:main'
            'GUINode = rover_gui.RoverGUI:main'
        ],
    },
)
