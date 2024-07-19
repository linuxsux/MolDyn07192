from openmm import Platform

available_platforms = Platform.findPlatform()
print("Available Platforms:", available_platforms)
