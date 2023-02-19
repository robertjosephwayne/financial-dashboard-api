from strategies.moving_average_crossover import MovingAverageCrossoverStrategy

moving_average_crossover = MovingAverageCrossoverStrategy(
    sma_fast_minutes=12 * 60, sma_slow_minutes=24 * 60, usd_per_trade=100
)


async def process_bar(symbol):
    await moving_average_crossover.process_bar(symbol)
