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
@click.option('--host', type=str, default='127.0.0.1', help='Host')
@click.option('--port', type=int, default=5000, help='Port')
def start_server(port, host):
    """Start tastehood server."""
    uvicorn.run("tastehood_server.server:app", host=host, port=port, log_level="info")


