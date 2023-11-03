import click
from agent import train

@click.command()
@click.option('-s', '--speed', default=20, help='Game speed')
def main(speed: int):
    settings = {
        "speed": speed
    }
    train(settings)

if __name__ == '__main__':
    main()