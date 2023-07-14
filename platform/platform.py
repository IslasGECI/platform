import typer
import platform as idp

platform = typer.Typer(help="Internal Developer Platform")


@platform.command()
def links():
    """
    - [Blog](https://islas.dev/blog/) \n
    - [Forum](https://github.com/IslasGECI/Foro/discussions) \n
    - [Manual](https://github.com/IslasGECI/manual) \n
    """
    pass


@platform.command()
def version():
    version = idp.__version__
    print(version)
