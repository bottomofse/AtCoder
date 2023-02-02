## [Educational DP Contest ](https://atcoder.jp/contests/dp) 

| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| [A - Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a) | [提出1](https://atcoder.jp/contests/dp/submissions/21574844) | 動的計画法 | 足場iでの最小コストはi-1とi-2から計算する |
| [B - Frog 2](https://atcoder.jp/contests/dp/tasks/dp_b) | [提出1](https://atcoder.jp/contests/dp/submissions/21575155) | 動的計画法 | A問題とほぼ同等の考え方 |
| [C - Vacation](https://atcoder.jp/contests/dp/tasks/dp_c) | [提出1](https://atcoder.jp/contests/dp/submissions/21575374) | 動的計画法 | ABCで別のdp配列を用意 |
| [D - Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d) | [提出1](https://atcoder.jp/contests/dp/submissions/23317759) [提出2](https://atcoder.jp/contests/dp/submissions/23317906) | 動的計画法 |  |
| [E - Knapsack 2](https://atcoder.jp/contests/dp/tasks/dp_e) | [提出1](https://atcoder.jp/contests/dp/submissions/23318654) | 動的計画法 |  |
| [F - LCS](https://atcoder.jp/contests/dp/tasks/dp_f) | [提出1](https://atcoder.jp/contests/dp/submissions/37854422) | 動的計画法 |  |
| []() | []() |  |  |

## [典型９０問](https://atcoder.jp/contests/typical90)

| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| [004 - Cross Sum（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_d) | [提出1](https://atcoder.jp/contests/typical90/submissions/33748596) |  | 行ごとの合計値、列ごとの合計値を先に計算しておき、各マスごとに行の合計値・列の合計値を加算しますの値を減算する |
| [010 - Score Sum Queries（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_j) | [提出1](https://atcoder.jp/contests/typical90/submissions/33749476) | 累積和 | 各組ごとの累積和を計算し、範囲の右端の値から左の範囲外の数値を引く |
| []() | []() |  |  |

## [AtCoder Beginner Contest 170](https://atcoder.jp/contests/abc170)

| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| [A - Five Variables](https://atcoder.jp/contests/abc170/tasks/abc170_a) | [提出1](https://atcoder.jp/contests/abc170/submissions/21853622) |  |  |
| [B - Crane and Turtle](https://atcoder.jp/contests/abc170/tasks/abc170_b) | [提出1](https://atcoder.jp/contests/abc170/submissions/21853531) |  |  |
| [C - Forbidden List](https://atcoder.jp/contests/abc170/tasks/abc170_c) | [提出1](https://atcoder.jp/contests/abc170/submissions/21853159) | 全探索 |  |
| [D - Not Divisible](https://atcoder.jp/contests/abc170/tasks/abc170_d) | [提出1](https://atcoder.jp/contests/abc170/submissions/37725905) | エラトステネスの篩 | データを昇順でソートした後篩で記録し倍数に該当しないiをカウントする |
| []() | []() |  |  |

## [AtCoder Beginner Contest 171](https://atcoder.jp/contests/abc171)

| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| [A - αlphabet](https://atcoder.jp/contests/abc171/tasks/abc171_a) | [提出1](https://atcoder.jp/contests/abc171/submissions/21852584) |  |  |
| [B - Mix Juice](https://atcoder.jp/contests/abc171/tasks/abc171_b) | [提出1](https://atcoder.jp/contests/abc171/submissions/21852542) |  |  |
| [C - One Quadrillion and One Dalmatians](https://atcoder.jp/contests/abc171/tasks/abc171_c) | [提出1](https://atcoder.jp/contests/abc171/submissions/21852372) |  | 整数を26進法で計算しアルファベットに変換する、ただし桁の境界に考慮必要 |
| [D - Replacing](https://atcoder.jp/contests/abc171/tasks/abc171_d) | [提出1](https://atcoder.jp/contests/abc171/submissions/37726933) | 差分更新 | 値ごとの数と合計値を計算しておき変換ごとに差分を計算する |
| []() | []() |  |  |

## [AtCoder Beginner Contest 172](https://atcoder.jp/contests/abc172)

| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| [A - Calc](https://atcoder.jp/contests/abc172/tasks/abc172_a) | [提出1](https://atcoder.jp/contests/abc172/submissions/21842120) |  |  |
| [B - Minor Change](https://atcoder.jp/contests/abc172/tasks/abc172_b) | [提出1](https://atcoder.jp/contests/abc172/submissions/21842115) |  |  |
| [C - Tsundoku](https://atcoder.jp/contests/abc172/tasks/abc172_c) | [提出1](https://atcoder.jp/contests/abc172/submissions/21842099) | 尺取り法・二分探索 | <br>※二分探索でもできるようだが未実装 |
| [D - Sum of Divisors](https://atcoder.jp/contests/abc172/tasks/abc172_d) | [提出1](https://atcoder.jp/contests/abc172/submissions/37729744) [提出2](https://atcoder.jp/contests/abc172/submissions/37729278) | エラトステネスの篩・等差数列の和 | 篩を使う場合、1の倍数をNまで加算、2の倍数を～でNまで行い最後に計算する<br>等差数列で考える場合は「初項1、公差1の数列の合計」「初項2、公差2の数列の合計」とNまで計算して加算する |
| []() | []() |  |  |

## [AtCoder Beginner Contest 173](https://atcoder.jp/contests/abc173)

| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| [A - Payment](https://atcoder.jp/contests/abc173/tasks/abc173_a) | [提出1](https://atcoder.jp/contests/abc173/submissions/21757363) |  |  |
| [B - Judge Status Summary](https://atcoder.jp/contests/abc173/tasks/abc173_b) | [提出1](https://atcoder.jp/contests/abc173/submissions/21757459) |  |  |
| [C - H and V](https://atcoder.jp/contests/abc173/tasks/abc173_c) | [提出1](https://atcoder.jp/contests/abc173/submissions/21761771) [提出2](https://atcoder.jp/contests/abc173/submissions/37697806) | bit全探索 |  |
| [D - Chat in a Circle](https://atcoder.jp/contests/abc173/tasks/abc173_d) | [提出1](https://atcoder.jp/contests/abc173/submissions/37698606) | 貪欲法 | 降順にソートしてから計算する |
| []() | []() |  |  |

## [エイシングプログラミングコンテスト](https://atcoder.jp/contests/aising2020)

| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| [A - Number of Multiples](https://atcoder.jp/contests/aising2020/tasks/aising2020_a) | [提出1](https://atcoder.jp/contests/aising2020/submissions/21779364) |  |  |
| [B - An Odd Problem](https://atcoder.jp/contests/aising2020/tasks/aising2020_b) | [提出1](https://atcoder.jp/contests/aising2020/submissions/21779339) |  |  |
| [C - XYZ Triplets](https://atcoder.jp/contests/aising2020/tasks/aising2020_c) | [提出1](https://atcoder.jp/contests/aising2020/submissions/21779307) | 全探索 | x,y,zを100以下で全探索する |
| [D - Anything Goes to Zero](https://atcoder.jp/contests/aising2020/tasks/aising2020_d) | []() |  |  |
| []() | []() |  |  |

## [M-SOLUTIONS プロコンオープン 2020](https://atcoder.jp/contests/m-solutions2020)

| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| [A - Kyu in AtCoder](https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_a) | [提出1](https://atcoder.jp/contests/m-solutions2020/submissions/21779644) |  |  |
| [B - Magic 2](https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_b) | [提出1](https://atcoder.jp/contests/m-solutions2020/submissions/21779623) |  |  |
| [C - Marks](https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_c) | [提出1](https://atcoder.jp/contests/m-solutions2020/submissions/21779553) |  | 例えば、例1の3学期の成績は、1x2x3学期の成績、4学期の成績は2x3x4学期の成績となるので、1学期と4学期の成績を比較すればよい |
| [D - Road to Millionaire](https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_d) | [提出1](https://atcoder.jp/contests/m-solutions2020/submissions/37741374) |  | 翌日上がる場合は買えるだけい買い、下がる場合はすべて売るを繰り返す。最後に株券を持っている場合はすべて売る |
| []() | []() |  |  |

## [AtCoder Beginner Contest 174](https://atcoder.jp/contests/abc174)

| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| [A - Air Conditioner](https://atcoder.jp/contests/abc174/tasks/abc174_a) | [提出1](https://atcoder.jp/contests/abc174/submissions/21722105) |  |  |
| [B - Distance](https://atcoder.jp/contests/abc174/tasks/abc174_b) | [提出1](https://atcoder.jp/contests/abc174/submissions/21722068) |  |  |
| [C - Repsept](https://atcoder.jp/contests/abc174/tasks/abc174_c) | [提出1](https://atcoder.jp/contests/abc174/submissions/21721825) | 合同式の性質 | 77は7の余りを10倍し7加算した値の余りを計算する、その余りを777の計算に利用する |
| [D - Alter Altar](https://atcoder.jp/contests/abc174/tasks/abc174_d) | [提出1](https://atcoder.jp/contests/abc174/submissions/37741751) |  | 左から白の石、右から赤の石を探索し交換していく |
| []() | []() |  |  |

## [AtCoder Beginner Contest 175](https://atcoder.jp/contests/abc175)

| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| [A - Rainy Season](https://atcoder.jp/contests/abc175/tasks/abc175_a) | [提出1](https://atcoder.jp/contests/abc175/submissions/21605643) |  |  |
| [B - Making Triangle](https://atcoder.jp/contests/abc175/tasks/abc175_b) | [提出1](https://atcoder.jp/contests/abc175/submissions/19574438) |  |  |
| [C - Walking Takahashi](https://atcoder.jp/contests/abc175/tasks/abc175_c) | [提出1](https://atcoder.jp/contests/abc175/submissions/21605589) |  |  |
| [D - Moving Piece](https://atcoder.jp/contests/abc175/tasks/abc175_d) | []() |  |  |
| []() | []() |  |  |

## [AtCoder Beginner Contest 176](https://atcoder.jp/contests/abc176)
| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| [A - Takoyaki](https://atcoder.jp/contests/abc176/tasks/abc176_a) | [提出1](https://atcoder.jp/contests/abc176/submissions/21589975) |  |  |
| [B - Multiple of 9](https://atcoder.jp/contests/abc176/tasks/abc176_b) | [提出1](https://atcoder.jp/contests/abc176/submissions/21589928) |  |  |
| [C - Step](https://atcoder.jp/contests/abc176/tasks/abc176_c) | [提出1](https://atcoder.jp/contests/abc176/submissions/21589857) |  |  |
| [D - Wizard in Maze](https://atcoder.jp/contests/abc176/tasks/abc176_d) | []() |  |  |

| 問題リンク | 提出リンク | 必要なアルゴリズム等 | メモ |
-|-|-|-
| []() | []() |  |  |
