# xxxor

The script then generates three random keys:

1. `key1` is a random byte string of the same length as `FLAG`.
2. `key2` is another random byte string of the same length as `FLAG`.
3. `key3` is the result of XORing `key1` and `key2`.

Finally, the script prints out three cipher texts:

1. `cipher1`: The result of XORing `FLAG` with `key1`.
2. `cipher2`: The result of XORing `FLAG` with `key2`.
3. `cipher3`: The result of XORing `FLAG` with `key3`.

Given the nature of the XOR operation, if we have two of the ciphers and one of the keys, we can retrieve the `FLAG`.

Next, let's examine the contents of the `xxxor.txt` file.

The `xxxor.txt` file contains three cipher texts:

1. `cipher1:0ad9aba65c1513e30afdd562e15890b02447832a204309bc1709d1`
2. `cipher2:be1854e0bbdb439920c174b445eadd287cd8e0d2c7062e679b1538`
3. `cipher3:fa82b413a49a16015263d9e6d6ed35c72ff60fc9b82214ecd32c94`

To recover the `FLAG`, we can use the property of the XOR operation that states:
$$A \oplus B \oplus B = A$$

Given:

1. `cipher1` is `FLAG` XORed with `key1`.
2. `cipher2` is `FLAG` XORed with `key2`.
3. `cipher3` is `FLAG` XORed with `key3` (which is `key1` XORed with `key2`).

Using the above property, we can deduce:
$$FLAG = cipher1 \oplus key1$$
$$FLAG = cipher2 \oplus key2$$
$$FLAG = cipher3 \oplus (key1 \oplus key2)$$

Thus, if we XOR `cipher1` with `cipher3`, we get:
$$cipher1 \oplus cipher3 = FLAG \oplus key1 \oplus (FLAG \oplus (key1 \oplus key2))$$
$$= FLAG \oplus FLAG \oplus key1 \oplus key1 \oplus key2$$
$$= key2$$

Now, XOR-ing `cipher2` with `key2` will give us the `FLAG`.

Let's go ahead and compute the `FLAG`.

The recovered flag is:

$$\text{NCKUCTF\{x\_x0r\_x\_wil1\_g37\_0\}}$$
