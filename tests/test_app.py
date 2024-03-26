'''Test cases of different operations performed'''
import pytest

from app import App

def get_environment_variable():
    '''Test how the REPL handles the command.'''
    app = App()
#   Retrieve the current environment setting
    current_env = app.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def add_command(capfd, monkeypatch):
    """Test how the REPL handles an add command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['addition', '2', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "The result of the operations is 4" in captured.out


def subtract_command(capfd, monkeypatch):
    """Test how the REPL handles a subtract command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['subtraction', '2', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "The result of the operations is 0" in captured.out


def multiply_command(capfd, monkeypatch):
    """Test how the REPL handles a multiply command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['multiply', '2', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "The result of the operation is 4" in captured.out


def division_command(capfd, monkeypatch):
    """Test how the REPL handles a divide command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['division', '2', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "The result of the operation is 1 " in captured.out

def fetch_command(capfd, monkeypatch):
    """Test how the REPL handles an fetch command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['fetch', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "Calculator history data:" in captured.out

def delete_command(capfd, monkeypatch):
    """Test how the REPL handles an delete command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['delete', 2, 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "After delete operation, the history of the calculator is:" in captured.out

def clear_command(capfd, monkeypatch):
    """Test how the REPL handles an clear command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['clear', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "History is cleared!" in captured.out

def menu_command(capfd, monkeypatch):
    """Test how the REPL handles an menu command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "The Menu options are:" in captured.out
