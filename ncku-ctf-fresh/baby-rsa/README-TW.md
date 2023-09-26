# RSA 挑戰文章

## 介紹

RSA 加密是公鑰加密的一種形式，它使用大素數的數學特性來加密和解密資料。 雖然 RSA 對於大質數是安全的，但使用較小的數字或弱參數可能會有漏洞。

## 挑戰

我們從 RSA 實作中獲得了 $p$、$q$、$e$ 和 $c$ 的值：

- $p$ 和 $q$：RSA 中使用的兩個質數。
- $e$ ：公共指數（通常設定為 65537）。
- $c$ ：密文（加密訊息）。

目標是解密密文$c$並檢索原始訊息。

## 方法

### 1. **計算 $n$ 和 $\varphi(n)$:**

- 計算$n = p \times q$。 該值用作公鑰和私鑰的模數。
- 計算totient $\varphi(n) = (p-1)(q-1)$。 這用於確定私鑰。

### 2. **計算私鑰 $d$:**

- 私有指數 $d$ 是 $e$ 模 $\varphi(n)$ 的模乘元。
- 這代表著 $d \times e \equiv 1 \mod \varphi(n)$。

### 3. **解密訊息：**

- 原始明文訊息$( M )$可以透過計算$M = c^d \mod n$找到。

### 4. **將數字轉換為文字：**

- 解密後的值是一個很大的數字，這表示原始訊息可能已被編碼為文字字串的數字表示形式。
- 使用 Crypto 庫中的“long_to_bytes”函數，該數字被轉換回其原始字串格式。

## 解決方案

按照上述方法，解密後的 flag 為：

`NCKUCTF{t0O_345y?Go_try_puRely high School mAth}`