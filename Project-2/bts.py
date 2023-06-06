import plotly.express as px

countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]
colors = ["green", "red", "blue", "yellow"]

# Define borders 
neighbors = { 
    "Argentina": ["Bolivia", "Brazil", "Chile", "Paraguay", "Uruguay"],
    "Bolivia": ["Argentina", "Brazil", "Chile", "Paraguay", "Peru"],
    "Brazil": ["Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
    "Chile": ["Argentina", "Bolivia", "Peru"],
    "Colombia": ["Brazil", "Ecuador", "Peru", "Venezuela"],
    "Ecuador": ["Colombia", "Peru"],
    "Falkland Islands": [],
    "Guyana": ["Brazil", "Suriname", "Venezuela"],
    "Paraguay": ["Argentina", "Bolivia", "Brazil"],
    "Peru": ["Bolivia", "Brazil", "Chile", "Colombia", "Ecuador"],
    "Suriname": ["Brazil", "Guyana"],
    "Uruguay": ["Argentina", "Brazil"],
    "Venezuela": ["Brazil", "Colombia", "Guyana"]
}

# Backtracking algorithm
def backtrack(country, colormap): 
    for color in colors:
        is_valid = True
        for neighbor in neighbors[country]:
            if neighbor in colormap and colormap[neighbor] == color:
                is_valid = False
                break
        if is_valid:
            colormap[country] = color
            next_country = next((c for c in countries if c not in colormap), None)
            if next_country is None or backtrack(next_country, colormap):
                return True
            del colormap[country]

    return False

# Plot choropleth map
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()

if __name__ == "__main__":
    colormap = {}
    backtrack(countries[0], colormap)
    plot_choropleth(colormap)