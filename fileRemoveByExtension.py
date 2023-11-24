import sys
from pathlib import Path


def delete_files_by_extension(extensions, path="."):
    """Delete files with given extensions in the specified path."""
    deleted_file_count = 0
    log = ""

    p = Path(path)
    for ext in extensions:
        file_list = list(p.rglob(f"*.{ext}"))

        if not file_list:
            print(f"NO {ext.upper()} FILES TO REMOVE.")
            continue

        print(f"Removing: {ext.upper()}")
        for file in file_list:
            if file.is_file():
                file.unlink()
                deleted_file_count += 1
                print(file)
                log += f"{file}\n"

        print("\n", end="")

    log += f"{deleted_file_count} FILES DELETED.\n"
    return log, deleted_file_count


def write_log(log, filename="delete_log.log"):
    """Write the log to a file."""
    if log:
        with open(filename, "a") as log_file:
            log_file.write(log)


def main():
    if len(sys.argv) > 1:
        log, deleted_file_count = delete_files_by_extension(sys.argv[1:])
        write_log(log)
    else:
        sys.exit("NO ARGUMENT PASSED.")


if __name__ == "__main__":
    main()
