async def process_data():
    """Processes some data asynchronously."""
    return "Processed Data"


def run():
    data = await process_data()  # ❌ Incorrect: `await` used outside async function
    print(data)
