def cat_files(dst_file, *src_files):
    with open(dst_file, "w") as f_out:
        for f in src_files:
            with open(f) as f_in:
                f_out.write(f_in.read())
