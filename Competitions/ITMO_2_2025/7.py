def solve():
    t = int(input().strip())
    results = []

    def read_card(tokens):
        return tokens.pop(0), tokens.pop(0)

    for _ in range(t):
        tokens = input().strip().split()
        n, a, q = int(tokens.pop(0)), int(tokens.pop(0)), int(tokens.pop(0))
        init_card = read_card(tokens)
        hands = [list(read_card(tokens) for _ in range(a)) for _ in range(n)]
        top_card = init_card
        current_player_idx = 0
        direction = 1
        chain_type = None
        chain_count = 0
        skip_next = False
        out_of_game = [False] * n

        def next_turn_idx(curr):
            return (curr + direction) % n

        def can_play(top, new):
            if top[1] == '@' or new[1] == '@':
                return True
            return top[0] == new[0] or top[1] == new[1]

        violation_found = False
        violation_msg = ""
        violation_player = 0
        violation_turn_num = 0

        for turn_i in range(1, q + 1):
            if violation_found:
                tokens = input().strip().split()
                if tokens[0] == '->':
                    if tokens[3] == 'AND':
                        tokens = tokens[7:]
                    else:
                        tokens = tokens[5:]
                elif tokens[0] == '<<-':
                    k = int(tokens[1])
                    tokens = tokens[3 + 2 * k:]
                continue

            tokens = input().strip().split()
            if tokens[0] == '->':
                tokens.pop(0)
                color, value = tokens.pop(0), tokens.pop(0)
                said_uno = False
                if tokens[0] == 'AND':
                    said_uno = True
                    tokens = tokens[2:]
                tokens.pop(0)
                i_player = int(tokens.pop(0))
                i_idx = i_player - 1
                if (color, value) not in hands[i_idx]:
                    violation_found = True
                    violation_msg = "no such card"
                    violation_player = i_player
                    violation_turn_num = turn_i
                    continue
                if i_idx != current_player_idx:
                    if out_of_game[i_idx]:
                        violation_found = True
                        violation_msg = "other player's turn"
                        violation_player = i_player
                        violation_turn_num = turn_i
                        continue
                    if (color, value) == top_card:
                        if value in ['X', '@']:
                            chain_type = value
                            chain_count = 1
                        else:
                            chain_type = None
                            chain_count = 0
                        hands[i_idx].remove((color, value))
                        top_card = (color, value)
                        cards_left = len(hands[i_idx])
                        if cards_left == 1 and not said_uno:
                            violation_found = True
                            violation_msg = "failed 'Uno!'"
                            violation_player = i_player
                            violation_turn_num = turn_i
                            continue
                        if cards_left != 1 and said_uno:
                            violation_found = True
                            violation_msg = "failed 'Uno!'"
                            violation_player = i_player
                            violation_turn_num = turn_i
                            continue
                        if cards_left == 0:
                            out_of_game[i_idx] = True
                        current_player_idx = i_idx
                        if value == '#':
                            skip_next = True
                        current_player_idx = next_turn_idx(current_player_idx)
                    else:
                        violation_found = True
                        violation_msg = "other player's turn"
                        violation_player = i_player
                        violation_turn_num = turn_i
                        continue
                else:
                    if chain_type is not None and chain_count > 0:
                        if value != chain_type:
                            violation_found = True
                            violation_msg = "wrong move"
                            violation_player = i_player
                            violation_turn_num = turn_i
                            continue
                        chain_count += 1
                        hands[i_idx].remove((color, value))
                        top_card = (color, value)
                        cards_left = len(hands[i_idx])
                        if cards_left == 1 and not said_uno:
                            violation_found = True
                            violation_msg = "failed 'Uno!'"
                            violation_player = i_player
                            violation_turn_num = turn_i
                            continue
                        if cards_left != 1 and said_uno:
                            violation_found = True
                            violation_msg = "failed 'Uno!'"
                            violation_player = i_player
                            violation_turn_num = turn_i
                            continue
                        if cards_left == 0:
                            out_of_game[i_idx] = True
                        current_player_idx = next_turn_idx(current_player_idx)
                    else:
                        if not can_play(top_card, (color, value)):
                            violation_found = True
                            violation_msg = "non-matching card"
                            violation_player = i_player
                            violation_turn_num = turn_i
                            continue
                        hands[i_idx].remove((color, value))
                        top_card = (color, value)
                        cards_left = len(hands[i_idx])
                        if cards_left == 1 and not said_uno:
                            violation_found = True
                            violation_msg = "failed 'Uno!'"
                            violation_player = i_player
                            violation_turn_num = turn_i
                            continue
                        if cards_left != 1 and said_uno:
                            violation_found = True
                            violation_msg = "failed 'Uno!'"
                            violation_player = i_player
                            violation_turn_num = turn_i
                            continue
                        if cards_left == 0:
                            out_of_game[i_idx] = True
                        if value == '#':
                            skip_next = True
                        if value == 'X':
                            chain_type = 'X'
                            chain_count = 1
                        elif value == '@':
                            chain_type = '@'
                            chain_count = 1
                        else:
                            chain_type = None
                            chain_count = 0
                        current_player_idx = next_turn_idx(current_player_idx)
            elif tokens[0] == '<<-':
                tokens.pop(0)
                k = int(tokens.pop(0))
                drawn_cards = []
                for _ in range(k):
                    ccol = tokens.pop(0)
                    cval = tokens.pop(0)
                    drawn_cards.append((ccol, cval))
                tokens.pop(0)
                i_player = int(tokens.pop(0))
                i_idx = i_player - 1
                if i_idx != current_player_idx:
                    violation_found = True
                    violation_msg = "other player's turn"
                    violation_player = i_player
                    violation_turn_num = turn_i
                    continue
                if chain_type == 'X' and chain_count > 0:
                    need = 2 * chain_count
                    if k != need:
                        violation_found = True
                        violation_msg = "wrong move"
                        violation_player = i_player
                        violation_turn_num = turn_i
                        continue
                    chain_type = None
                    chain_count = 0
                    hands[i_idx].extend(drawn_cards)
                    current_player_idx = next_turn_idx(current_player_idx)
                elif chain_type == '@' and chain_count > 0:
                    need = 4 * chain_count
                    if k != need:
                        violation_found = True
                        violation_msg = "wrong move"
                        violation_player = i_player
                        violation_turn_num = turn_i
                        continue
                    chain_type = None
                    chain_count = 0
                    hands[i_idx].extend(drawn_cards)
                    current_player_idx = next_turn_idx(current_player_idx)
                else:
                    if k != 1:
                        violation_found = True
                        violation_msg = "wrong move"
                        violation_player = i_player
                        violation_turn_num = turn_i
                        continue
                    hands[i_idx].extend(drawn_cards)
                    current_player_idx = next_turn_idx(current_player_idx)

        if violation_found:
            results.append(f"{violation_msg} BY player {violation_player} ON turn {violation_turn_num}")
        else:
            results.append("no violations")

    print("\n".join(results))
solve()
