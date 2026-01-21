## RH‑LOCAL (G‑8) — Explicit unconditional local zero‑window bounds for v32’s local term

### 1) Where this plugs into v32 (anchor points)

In v32 Part II, the **local window** and **local factor** are:

- \(Z(m):=\{\rho:\ E(\rho)=0,\ |\Im \rho - m|\le 1\}\) (zeros counted with multiplicity)  
- \(Z_{\mathrm{loc}}(v):=\prod_{\rho\in Z(m)}(v-\rho)^{m_\rho}\), and residual \(F(v):=E(v)/Z_{\mathrm{loc}}(v)\).【517:1†manuscript_v32.pdf†L24-L34】

In Section 10, v32 then uses:

- **Buffered local log‑derivative bound** (your Lemma 10.5):  
  \[
  \sup_{\partial B}\left|\frac{Z'_{\mathrm{loc}}(v)}{Z_{\mathrm{loc}}(v)}\right|\le \frac{N_{\mathrm{loc}}(m)}{\kappa\,\delta},
  \]
  where \(N_{\mathrm{loc}}(m)\) counts zeros in the local window (with multiplicity).【517:7†manuscript_v32.pdf†L29-L48】

- and the **outer‑aligned upper envelope** (your Corollary 10.7) introduces the local term:
  \[
  \sum_\pm |W(v_\pm)-e^{i\phi_0^\pm}|
  \ \le\ 2C_{\mathrm{up}}\Bigl(\delta^{3/2}L(m)+\delta^{1/2}\frac{N_{\mathrm{loc}}(m)}{\kappa}\Bigr).\tag{v32}
  \]【517:7†manuscript_v32.pdf†L56-L69】

So to close **G‑8**, we only need an explicit unconditional bound for \(N_{\mathrm{loc}}(m)\) of the form
\[
N_{\mathrm{loc}}(m)\ \le\ A_N\log m + B_N \quad (m\ge m_0),
\]
with explicit \((A_N,B_N,m_0)\), and then the local term becomes explicit.

---

## 2) The explicit unconditional bound (zero window)

### 2.1 External explicit input (published)

Let \(N(T)\) denote the number of nontrivial zeros \(\rho=\beta+i\gamma\) of \(\zeta(s)\) with \(0<\gamma\le T\), counted with multiplicity.

Bellotti–Wong (2024/2025) give an explicit bound for the zero‑counting function: for every \(T\ge e\),
\[
\Bigl|\,N(T)-\frac{T}{2\pi}\log\!\Bigl(\frac{T}{2\pi e}\Bigr)\Bigr|
\ \le\ 0.10076\log T\ +\ 0.24460\log\log T\ +\ 8.08344.
\] citeturn6view0

This is unconditional (no RH assumption).

### 2.2 Derived “two‑unit interval” bound \(N(T+1)-N(T-1)\)

Define \(M(T):=\dfrac{T}{2\pi}\log\!\bigl(\dfrac{T}{2\pi e}\bigr)\). Then
\[
M'(T)=\frac{1}{2\pi}\log\!\Bigl(\frac{T}{2\pi}\Bigr).
\]

For \(T\ge 5\), using \(\log\log x\le \log x\) for \(x\ge e\) and \(\log(T\pm 1)\le \log(2T)\) for \(T\ge 1\), one obtains the explicit estimate
\[
N(T+1)-N(T-1)\ \le\ 1.00903\,\log T\ +\ 16.8663
\ \le\ 1.01\,\log T\ +\ 17.
\tag{★}
\]

(Details are in the paste‑ready proof below; the only external ingredient is the Bellotti–Wong bound.)

This implies the requested template bound \(N(T+H)-N(T-H)\le A\log T + B\) for all \(0<H\le 1\) simply because
\[
N(T+H)-N(T-H)\ \le\ N(T+1)-N(T-1),
\]
so the same \(A,B\) work.

---

## 3) Mapping to v32 parameters \((m,\delta,\kappa,\alpha)\) and \(N_{\mathrm{loc}}(m)\)

### 3.1 Width–2 conversion

In your width–2 frame, \(m=2T\) where \(T\) is the classical ordinate (imaginary part in the \(s\)-plane). This conversion is explicit already in your v29+ manuscripts and used in v32.【517:7†manuscript_v32.pdf†L52-L55】

Your local window in v32 is:
\[
|\Im \rho_v - m|\le 1 \quad\Longleftrightarrow\quad |\gamma - T|\le \tfrac12
\]
for the corresponding \(\zeta\)-zero ordinate \(\gamma\). Therefore
\[
N_{\mathrm{loc}}(m)=N(T+\tfrac12)-N(T-\tfrac12)\ \le\ N(T+1)-N(T-1).
\]

### 3.2 Explicit \(N_{\mathrm{loc}}(m)\) bound

Let \(m\ge 10\). Then \(T=m/2\ge 5\), and applying (★):
\[
N_{\mathrm{loc}}(m)
\ \le\ 1.01\log(T)\ +\ 17
\ =\ 1.01\log(m/2)+17
\ \le\ 1.01\log m\ +\ 17.
\tag{Nloc‑exp}
\]

So one valid explicit choice is:
\[
A_N = 1.01,\qquad B_N = 17,\qquad m_0=10.
\]

---

## 4) Translation to the manuscript’s local term \( \sup_{\partial B} |Z'_{\mathrm{loc}}/Z_{\mathrm{loc}}| \)

Using v32 Lemma 10.5 on a \(\kappa\)-admissible box \(B(\alpha,m,\delta)\),
\[
\sup_{\partial B}\left|\frac{Z'_{\mathrm{loc}}}{Z_{\mathrm{loc}}}\right|
\ \le\ \frac{N_{\mathrm{loc}}(m)}{\kappa\delta}
\ \le\ \frac{1.01\log m + 17}{\kappa\delta},
\qquad (m\ge 10).
\tag{Zloc‑logder‑exp}
\]
This is exactly the explicit input needed for the local term in Corollary 10.7.【517:7†manuscript_v32.pdf†L56-L69】

### 4.1 “How it plugs into the tail inequality” (explicitly)

v32’s envelope already isolates the local contribution as \(\delta^{1/2}N_{\mathrm{loc}}(m)/\kappa\).【517:7†manuscript_v32.pdf†L56-L69】

With (Nloc‑exp), the corollary becomes (explicit local term):
\[
\sum_\pm |W(v_\pm)-e^{i\phi_0^\pm}|
\ \le\ 2C_{\mathrm{up}}
\left(
\delta^{3/2}L(m)\ +\ \frac{\delta^{1/2}}{\kappa}(1.01\log m + 17)
\right),
\quad m\ge 10.
\tag{tail‑local‑explicit}
\]

Now map \(\delta\) to your parameters:
\[
\delta=\delta(m,\alpha)=\frac{\eta\alpha}{(\log m)^2},\quad \alpha\in(0,1],\ \eta\in(0,1).
\]【517:1†manuscript_v32.pdf†L16-L23】

Then
\[
\delta^{1/2}(1.01\log m + 17)
= \frac{\sqrt{\eta\alpha}}{\log m}(1.01\log m + 17)
= \sqrt{\eta\alpha}\left(1.01 + \frac{17}{\log m}\right).
\]
Hence for all \(m\ge 10\) (so \(\log m\ge \log 10\)) and \(\alpha\le 1\),
\[
\delta^{1/2}\frac{N_{\mathrm{loc}}(m)}{\kappa}
\ \le\ \frac{\sqrt{\eta}}{\kappa}\left(1.01 + \frac{17}{\log 10}\right)
\approx \frac{8.40}{\kappa}\sqrt{\eta}.
\tag{local‑term‑O(sqrtη)}
\]

This is the key “absorption‑friendly” scaling: the local term is **uniform in \(m\ge 10\)** and is explicitly \(O(\sqrt{\eta})\) (up to the collar factor \(1/\kappa\)). This supports δ‑uniform absorption *for the local term* (while global δ‑uniformity for the rest of the mechanism remains a separate branch obligation).

---

# Mandatory Patch Packet

- **Prompt Batch Number:** 1

- **Callsign:** RH-LOCAL

- **Result classification:** **PASS**  
  (G‑8 can be closed with an explicit, unconditional lemma-ready bound and explicit plug‑in to the local term.)

- **Target gaps closed (by ID):** **G‑8** (local window / local term bounds with explicit constants and ranges)

- **Target gaps still open (by ID):**  
  **G‑4** (global δ‑uniformity for absorption; this patch only supplies the explicit local contribution),  
  **G‑3** ( \(K_{\rm alloc}\) provenance),  
  **G‑6** (Bridge‑1 hypotheses regularity), and any remaining tail ledger obligations (e.g., certified \(C_1,C_2\)) not in scope.

- **Key conclusions (≤5 bullets):**
  1. v32’s local factor window is \(Z(m)=\{\rho:E(\rho)=0,\ |\Im\rho-m|\le 1\}\), giving \(N_{\rm loc}(m)\) as a short interval zero count.【517:1†manuscript_v32.pdf†L24-L34】
  2. Using Bellotti–Wong’s explicit zero-counting bound for \(N(T)\), one obtains for all \(T\ge 5\):  
     \(N(T+1)-N(T-1)\le 1.01\log T + 17\). citeturn6view0
  3. Therefore for all \(m\ge 10\): \(N_{\rm loc}(m)\le 1.01\log m + 17\).
  4. Plugging into v32 Lemma 10.5 yields \(\sup_{\partial B}|Z'_{\rm loc}/Z_{\rm loc}|\le (1.01\log m + 17)/(\kappa\delta)\).【517:7†manuscript_v32.pdf†L29-L48】
  5. The envelope’s local contribution becomes explicit and uniformly \(O(\sqrt{\eta}/\kappa)\) under \(\delta=\eta\alpha/(\log m)^2\).【517:7†manuscript_v32.pdf†L56-L69】

---

## Paste-ready manuscript edits

### (i) Lemma statement (replace v32 Lemma 10.6)

```tex
\begin{lemma}[Explicit local window zero count]\label{lem:Nloc-explicit}
Let $N(T)$ denote the number of nontrivial zeros $\rho=\beta+i\gamma$ of $\zeta(s)$ with
$0<\gamma\le T$, counted with multiplicity. Then for every $T\ge 5$,
\begin{equation}\label{eq:two-unit-window}
N(T+1)-N(T-1)\le 1.01\log T + 17.
\end{equation}
Consequently, for every $m\ge 10$ and $N_{\mathrm{loc}}(m)$ as in \eqref{eq:Zloc-def}--\eqref{eq:F-def},
\begin{equation}\label{eq:Nloc-explicit}
N_{\mathrm{loc}}(m)\le 1.01\log m + 17.
\end{equation}
\end{lemma}
```

*(You will need to ensure the cross-references \(\eqref{eq:Zloc-def}\)–\(\eqref{eq:F-def}\) point to your equations (10)–(11) defining \(Z(m)\), \(Z_{\rm loc}\), \(F\). In v32 these are the displayed equations (10)–(11).【517:1†manuscript_v32.pdf†L24-L34】)*

### (ii) Proof paragraph (citation-based, explicit constants)

```tex
\begin{proof}
By \cite[Theorem~1.1]{BellottiWongZeta2024} (arXiv:2412.15470v2), for every $x\ge e$,
\[
\left|N(x)-\frac{x}{2\pi}\log\!\Bigl(\frac{x}{2\pi e}\Bigr)\right|
\le 0.10076\log x + 0.24460\log\log x + 8.08344.
\]
Let $M(x):=\frac{x}{2\pi}\log(\frac{x}{2\pi e})$. Then $M'(x)=\frac{1}{2\pi}\log(\frac{x}{2\pi})$.
For $T\ge 5$ we have
\[
M(T+1)-M(T-1)=\int_{T-1}^{T+1}M'(x)\,dx
\le \int_{T-1}^{T+1}\frac{1}{2\pi}\log x\,dx
\le \frac{1}{\pi}\log(2T).
\]
Using $\log\log x\le \log x$ for $x\ge e$ and $\log(T\pm 1)\le \log(2T)$ for $T\ge 1$, we obtain
\[
N(T+1)-N(T-1)\le (M(T+1)-M(T-1))
+2(0.10076+0.24460)\log(2T) + 2\cdot 8.08344,
\]
hence $N(T+1)-N(T-1)\le 1.00903\log T + 16.8663 \le 1.01\log T + 17$.
Finally, the v32 local window $|\Im\rho-m|\le 1$ corresponds to $|\gamma-m/2|\le 1/2$ in the $s$-plane,
so $N_{\mathrm{loc}}(m)\le N(m/2+1)-N(m/2-1)$, and \eqref{eq:Nloc-explicit} follows.
\end{proof}
```

### (iii) Inequality line in Corollary 10.7 (make the “≤” line explicit)

Replace the symbolic “\(A_N\log m+B_N\)” instantiation with:

```tex
\[
\sum_{\pm}|W(v_\pm)-e^{i\phi_0^\pm}|
\le 2C_{\mathrm{up}}
\left(\delta^{3/2}L(m)+\frac{\delta^{1/2}}{\kappa}(1.01\log m+17)\right),
\qquad (m\ge 10).
\]
```

Optionally add the scaling remark (useful for the absorption branch):

```tex
\begin{remark}
With $\delta=\eta\alpha/(\log m)^2$ and $\alpha\le 1$, one has
$\delta^{1/2}(1.01\log m+17)\le \sqrt{\eta}\left(1.01+\frac{17}{\log 10}\right)$ for all $m\ge 10$.
Thus the local contribution to the envelope is uniformly $O(\sqrt{\eta}/\kappa)$ in $m\ge 10$.
\end{remark}
```

### Bib entry (minimum viable)

```bibtex
@article{BellottiWongZeta2024,
  author        = {Chiara Bellotti and Peng-Jie Wong},
  title         = {Improved estimates for the argument and zero-counting function of the {R}iemann zeta-function},
  year          = {2024},
  eprint        = {2412.15470},
  archivePrefix = {arXiv},
  primaryClass  = {math.NT},
  note          = {See Theorem 1.1 for an explicit bound on $N(T)$}
}
```

---

## Dependencies on other branches

- **RH-ABSORB:** will use \(\delta^{1/2}N_{\rm loc}(m)/\kappa \ll \sqrt{\eta}/\kappa\) as an explicit, \(m\)-uniform local‑term input (this patch provides it; RH-ABSORB still must close global δ‑uniformity).  
- **RH-FORCE / RH-BRIDGE:** none directly, except they consume the same envelope inequality where this term appears.

---

## Referee risk notes

1. **Definition alignment:** Ensure manuscript \(N(T)\) counts zeros with multiplicity and \(0<\gamma\le T\) (standard). The mapping to \(m=2T\) is already in v32 and should remain explicit.【517:7†manuscript_v32.pdf†L52-L55】  
2. **Cross-reference hygiene:** v32 Lemma 10.4 currently references “(??)” for \(Z_{\rm loc},F\); it should cite equations (10)–(11).【517:7†manuscript_v32.pdf†L14-L28】【517:1†manuscript_v32.pdf†L24-L34】  
3. **External constant provenance:** This patch makes the local bound unconditional by citing Bellotti–Wong; the manuscript should treat it as a referenced explicit inequality, not as an “\(O(\log T)\)” placeholder. citeturn6view0
