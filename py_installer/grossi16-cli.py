#!/usr/bin/env python3

import sys
import click
from grossi16.web import main

@click.command()
def fake_main():
    main()

@click.pass_context
if __name__ == "__main__":
    fake_main()
