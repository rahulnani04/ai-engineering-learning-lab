"""Synthetic I/O workload; demonstrates cooperative concurrency."""
import asyncio
import time

async def simulated_lookup(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name}: synthetic completed"

async def main():
    tasks = [("policy", 0.2), ("account", 0.3), ("transaction", 0.5)]
    start = time.perf_counter()
    sequential = []
    for name, delay in tasks:
        sequential.append(await simulated_lookup(name, delay))
    seq_time = time.perf_counter() - start
    start = time.perf_counter()
    concurrent = await asyncio.gather(*(simulated_lookup(name, delay) for name, delay in tasks))
    concurrent_time = time.perf_counter() - start
    print("Sequential:", sequential, f"elapsed={seq_time:.2f}s")
    print("Concurrent:", concurrent, f"elapsed={concurrent_time:.2f}s")
    print("These are artificial sleeps, not measurements of production APIs.")

if __name__ == "__main__":
    asyncio.run(main())
