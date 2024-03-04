from multi_instance_terminal import terminal

main = terminal.create_terminal('__main__')
error = terminal.create_terminal('Error')
tx = terminal.create_terminal('TX Data (transmit)')
rx = terminal.create_terminal('RX Data (receive)')