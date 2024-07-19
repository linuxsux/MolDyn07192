from openmm import Platform

available_platforms = Platform.getPlatformNames()
print("Available Platforms:", available_platforms)