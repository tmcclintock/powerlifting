from distutils.core import setup

dist = setup(name="powerlifting",
             author="Tom McClintock",
             author_email="tmcclintock89@gmail.com",
             version="1.0.0",
             description="tools to analyze powerlifting",
             url="https://github.com/tmcclintock/powerlifting",
             packages=['powerlifting',],
             install_requires=['numpy','scipy']
)
