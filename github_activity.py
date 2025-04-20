import requests
import typer

app = typer.Typer()

@app.command()
def activity(username: str):
    url = f"https://api.github.com/users/{username}/events/public"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            typer.echo("Failed to fetch activity. Check username.")
            raise typer.Exit(code=1)
    except requests.RequestException as e:
        typer.echo("Failed to fetch activity. Network or API error.")
        raise typer.Exit(code=1)

    data = response.json()
    for event in data[:5]:
        typer.echo(f"{event['type']} at {event['created_at']} in {event['repo']['name']}")