def format_exception_message(e):
    if hasattr(e, "message") and e.message:
        return f"Error: {e.message}"
    elif hasattr(e, "args") and e.args:
        return f"Error: {', '.join(map(str, e.args))}"
    else:
        return f"Unexpected: {str(e)}"


def safe_block(function, params: dict = {}):
    # Runs small function _relatively_ safely
    try:
        function(**params)
    except Exception as e:
        # for now just print, TODO, exception handler via params or something
        print(format_exception_message(e))


def line_splitter(line):
    segregation = line.split(":", 1)
    author_info = segregation[0]
    message = segregation[1].replace("\n", "")
    print(f"Author info: {author_info}, message:{message}")
