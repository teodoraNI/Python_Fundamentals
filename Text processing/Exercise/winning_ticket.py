def is_ticket_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols =['@', '#', '$', '^']
    for symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_repetition = symbol * uninterrupted_match_length
            if winning_repetition in ticket[:10] and winning_repetition in ticket[10:]:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]
for ticket in tickets:
    print(is_ticket_winning(ticket))
