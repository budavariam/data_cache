import h5py

## CONFIG
def main():
    parent = "xxxx"
    todelete = [
    "xxxx",
    ]
    h5_file = "./data.h5"

    ## CODE

    with h5py.File(h5_file, "a") as f:
        x = f[parent]
        print(x)
        for child in todelete:
            if child in x:
                del x[child]
                print(f"INFO: '{child}' REMOVED from '{parent}'")
            else:
                print(f"WARN: '{child}' NOT FOUND in '{parent}'")
    print("DONE")

if __name__ == "__main__":
    main()