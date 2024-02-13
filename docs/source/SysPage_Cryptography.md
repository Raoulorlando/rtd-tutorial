##### <span id="index"></span>Cryptography

IBIS uses the Reindael encryption mechanism to hash and/or encrypt
sensitive data like passwords and plugin settings.

-   The cryptography settings are stored in the Cryptography folder,
    which resides in the App\_Data folder
-   The contents of this file can be altered from the Cryptography page
    in ~/Crypto)

**NOTE: in case you change the cryptography settings, make sure to copy
the default.crypt file to all servers in the system otherwise they will
be unable to perform cryptographic operations.**

<table class="table table-bordered">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead class="thead-light">
<tr class="header">
<th>Setting</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td width="170"><p>Passprase</p></td>
<td width="406"><p>A string of text used to encrypt the input:</p>
<ul>
<li>Long enough to be hard to guess</li>
<li>At least 56 characters for maximum security</li>
<li>Not a famous quotation from literature, holy books, etc.</li>
<li>Hard to guess by intuition</li>
<li>Not reused between sites, applications and other different
sources</li>
</ul></td>
</tr>
<tr class="even">
<td width="170"><p>Salt</p></td>
<td width="406"><p>Random data that is used as an additional input to a
one-way function that "hashes" data, a password or passphrase. Salts are
closely related to the concept of nonce. The primary function of salts
is to defend against dictionary attacks or against its hashed
equivalent, a pre-computed rainbow table attack.</p></td>
</tr>
<tr class="odd">
<td width="170"><p>Iterations</p></td>
<td width="406"><p>The number of iterations to use to derive the key. A
higher number should be more secure but takes longer to calculate. The
default is <strong>1000</strong></p></td>
</tr>
</tbody>
</table>
