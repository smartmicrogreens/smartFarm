#!python3
# -*- coding: utf-8 -*-
"""Command line interface for tastehood server."""
import uvicorn
import click


@click.group()
@click.version_option()
def main():
    pass


@main.command()
@click.help_option()
def start_server():
    """Start tastehood server."""
    uvicorn.run("tastehood_server.server:app", host="127.0.0.1", port=5000, log_level="info")



