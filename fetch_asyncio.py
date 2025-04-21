import asyncio
import aiohttp

def run_with_asyncio(url, output_box, status_label):
    async def fetch():
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    content = await response.text()
        except Exception as e:
            content = f"Error: {e}"

        def update_gui():
            output_box.config(state="normal")
            output_box.delete("1.0", "end")
            output_box.insert("1.0", content)
            output_box.config(state="disabled")
            status_label.config(text="Done!")

        output_box.after(0, update_gui)

    asyncio.run(fetch())
