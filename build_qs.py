import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract head and header
head_match = re.search(r'(<head>.*?</style>\s*</head>)', html, re.DOTALL)
header_match = re.search(r'(<header class="site-header">.*?</header>)', html, re.DOTALL)
footer_match = re.search(r'(<footer class="site-footer">.*?</footer>)', html, re.DOTALL)

head = head_match.group(1)
# modify title and desc
head = re.sub(r'<title>.*?</title>', '<title>Quick Start &mdash; Unfold</title>', head)
head = re.sub(r'<meta name="description".*?>', '<meta name="description" content="Unfoldのクイックスタートガイド。インストールから最初のコード解説を体験するまでの最短手順をご案内します。">', head)

header = header_match.group(1)
# modify nav links
header = header.replace('href="#features"', 'href="https://aigamecreators.github.io/unfold-site/#features"')
header = header.replace('href="#screenshots"', 'href="https://aigamecreators.github.io/unfold-site/#screenshots"')
header = header.replace('href="#faq"', 'href="https://aigamecreators.github.io/unfold-site/#faq"')
header = header.replace('<span class="nav-links">', '<span class="nav-links">\n                    <a href="https://aigamecreators.github.io/unfold-site/" class="nav-link">Home</a>')

footer = footer_match.group(1)

MAIN_CONTENT = """
    <main>
        <section class="hero" style="padding-bottom: 2rem;">
            <div class="container">
                <div class="hero-grid" style="grid-template-columns: 1fr; text-align: left;">
                    <div class="hero-content">
                        <div class="hero-badge">チュートリアル</div>
                        <h1 class="hero-title">
                            Quick Start
                        </h1>
                        <p class="hero-desc" style="max-width: 700px; font-size: 1.05rem;">
                            Unfold は、コードを一気に説明するAIではなく、<strong>「全体像 → 構造 → 詳細」の順で迷わず読むための学習ツール</strong>です。<br>
                            このページでは、インストールから最初のコード解説を表示するところまでを案内します。
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <hr class="divider">

        <section class="section" id="prerequisites">
            <div class="container">
                <div class="section-label">Prerequisites</div>
                <h2 class="section-title">前提条件</h2>

                <div class="notice-box" style="margin-top: 1.5rem;">
                    <p class="notice-heading" style="font-size: 1rem;">ご利用には以下の環境が必要です。</p>
                    <ul class="notice-list">
                        <li><strong>VS Code 1.107.0</strong> 以上</li>
                        <li>以下のいずれかのAIプロバイダー環境（ご自身で用意する BYOK 形式です）
                            <ul style="padding-left: 1.5rem; margin-top: 0.5rem; list-style-type: circle; color: var(--text-dim);">
                                <li style="margin-bottom: 0.3rem;"><code style="background: var(--bg-base); padding: 0.1rem 0.4rem; border-radius: 4px; border: 1px solid var(--border);">Gemini</code> のAPIキー</li>
                                <li style="margin-bottom: 0.3rem;"><code style="background: var(--bg-base); padding: 0.1rem 0.4rem; border-radius: 4px; border: 1px solid var(--border);">OpenRouter</code> のAPIキー</li>
                                <li style="margin-bottom: 0.3rem;"><code style="background: var(--bg-base); padding: 0.1rem 0.4rem; border-radius: 4px; border: 1px solid var(--border);">Ollama</code> のローカル実行環境</li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </section>

        <hr class="divider">

        <section class="section" id="steps">
            <div class="container">
                <div class="section-label">Steps</div>
                <h2 class="section-title">3分で試す手順</h2>
                <p class="section-desc">インストールから最初の解説を表示するまでの基本ステップです。</p>

                <!-- Step 1 -->
                <div style="margin-top: 3rem;">
                    <h3 style="color: var(--text-primary); font-family: var(--font-heading); font-size: 1.2rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.6rem;">
                        <span class="step-num" style="margin-bottom: 0;">1</span> 拡張機能をインストールする
                    </h3>
                    <ol style="padding-left: 1.5rem; color: var(--text-body); line-height: 1.9;">
                        <li style="margin-bottom: 0.4rem;">VS Code に Unfold 拡張機能をインストールします。</li>
                    </ol>
                </div>

                <!-- Step 2 -->
                <div style="margin-top: 3.5rem;">
                    <h3 style="color: var(--text-primary); font-family: var(--font-heading); font-size: 1.2rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.6rem;">
                        <span class="step-num" style="margin-bottom: 0;">2</span> プロバイダーとAPIキーを設定する
                    </h3>
                    <ol style="padding-left: 1.5rem; color: var(--text-body); line-height: 1.9; margin-bottom: 1.5rem;">
                        <li style="margin-bottom: 0.4rem;">アクティビティバーから <strong>Unfold</strong> のアイコンをクリックし、<strong>Settings（設定）</strong> を開きます。</li>
                        <li style="margin-bottom: 0.4rem;">使用するプロバイダーを選択し、<strong>APIキー</strong>を入力して保存します。</li>
                    </ol>
                    <div class="screenshot-frame" style="aspect-ratio: unset; max-width: 600px; padding: 0; background: transparent; border: 1px solid var(--border);">
                        <img src="images/screenshot_setting.png" alt="設定画面のスクリーンショット" width="811" height="1028" style="width: 100%; height: auto; display: block; border-radius: 8px;">
                    </div>
                </div>

                <!-- Step 3 -->
                <div style="margin-top: 4.5rem;">
                    <h3 style="color: var(--text-primary); font-family: var(--font-heading); font-size: 1.2rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.6rem;">
                        <span class="step-num" style="margin-bottom: 0;">3</span> コードを解説してみる
                    </h3>
                    <ol style="padding-left: 1.5rem; color: var(--text-body); line-height: 1.9; margin-bottom: 1.5rem;">
                        <li style="margin-bottom: 0.4rem;">エディタで、<strong>解説したいコードファイルを開いた状態</strong>にします。</li>
                        <li style="margin-bottom: 0.4rem;">Unfoldのサイドメニューから、<strong style="color: var(--accent); background: var(--accent-muted); border: 1px solid rgba(62,175,247,0.2); padding: 0.2rem 0.6rem; border-radius: 6px; display: inline-block; margin: 0 0.4rem;">「解説を開始する」</strong> ボタンを押します。</li>
                    </ol>
                    <div class="screenshot-frame" style="aspect-ratio: unset; max-width: 450px; padding: 0; background: transparent; border: 1px solid var(--border);">
                        <img src="images/screenshot_start.png" alt="解説を開始するボタンのスクリーンショット" width="889" height="822" style="width: 100%; height: auto; display: block; border-radius: 8px;">
                    </div>
                </div>

                <!-- Step 4 -->
                <div style="margin-top: 4.5rem;">
                    <h3 style="color: var(--text-primary); font-family: var(--font-heading); font-size: 1.2rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.6rem;">
                        <span class="step-num" style="margin-bottom: 0;">4</span> ガイドに沿ってコードを読む
                    </h3>
                    <p style="color: var(--text-body); margin-bottom: 2rem; font-size: 0.95rem;">生成が完了すると、サイドバーに解説が表示されます。</p>
                    
                    <div style="margin-bottom: 3rem; background: var(--bg-card); padding: 1.5rem; border-radius: 10px; border: 1px solid var(--border);">
                        <h4 style="color: var(--text-primary); font-size: 1.05rem; font-weight: 600; margin-bottom: 0.5rem;">まずは読み始めガイドを選ぶ</h4>
                        <p style="color: var(--text-dim); margin-bottom: 1.5rem;">まずはコード全体の概要を確認し、「どこから読めばいいか」の提案から最初のブロックを選んでみてください。</p>
                        
                        <div class="screenshot-frame" style="aspect-ratio: unset; max-width: 600px; padding: 0; background: transparent; border: 1px solid var(--border-light);">
                            <img src="images/screenshot3.png" alt="トップ画面のスクリーンショット" width="913" height="534" style="width: 100%; height: auto; display: block; border-radius: 8px;">
                        </div>
                    </div>

                    <div style="background: var(--bg-card); padding: 1.5rem; border-radius: 10px; border: 1px solid var(--border);">
                        <h4 style="color: var(--text-primary); font-size: 1.05rem; font-weight: 600; margin-bottom: 0.5rem;">ドリルダウンで詳細を確認</h4>
                        <p style="color: var(--text-dim); margin-bottom: 1.5rem; line-height: 1.8;">
                            ブロック詳細画面では詳しい解説が読めます。<br>
                            処理が複雑な場合は、さらに深掘り（ドリルダウン）してみましょう。エディタ上のコードも連動して<strong>ハイライト</strong>されます。
                        </p>
                        <div class="screenshot-frame" style="aspect-ratio: unset; max-width: 700px; padding: 0; background: transparent; border: 1px solid var(--border-light);">
                            <img src="images/screenshot2.png" alt="ブロック詳細画面のスクリーンショット" width="1398" height="865" style="width: 100%; height: auto; display: block; border-radius: 8px;">
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <hr class="divider">

        <section class="section" id="troubleshooting">
            <div class="container">
                <div class="section-label">Troubleshooting</div>
                <h2 class="section-title">よくあるつまずき</h2>
                <p class="section-desc">うまく動かない場合は、以下を確認してください。</p>
                
                <div class="faq-list" style="margin-top: 1.5rem;">
                    <div class="faq-item">
                        <h3 style="color: var(--accent); font-size: 1rem;">解説が生成されない / エラーになる</h3>
                        <p>Settings ビューで API キーが正しく入力されているか、プロバイダーとモデル名の組み合わせが合っているかを確認してください。</p>
                    </div>
                    <div class="faq-item">
                        <h3 style="color: var(--purple); font-size: 1rem;">Ollama が動かない</h3>
                        <p>ローカルで Ollama のアプリが起動しているか、指定したモデルが <code style="background: rgba(166,110,240,0.15); padding: 0.1rem 0.4rem; color: var(--purple); border-radius: 4px; font-family: monospace;">ollama run &lt;model&gt;</code> で手元にダウンロード済みかを確認してください。</p>
                    </div>
                    <div class="faq-item">
                        <h3 style="color: var(--accent); font-size: 1rem;">うまく説明が分割されない・長すぎる</h3>
                        <p>まずはファイル全体ではなく、1つの「関数」や「クラス」だけを選択して <code style="background: rgba(62,175,247,0.15); padding: 0.1rem 0.4rem; color: var(--accent); border-radius: 4px; font-family: monospace;">Unfold: Explain Selection</code> を試してみてください。</p>
                    </div>
                </div>
            </div>
        </section>

        <hr class="divider">

        <section class="section" id="next-steps">
            <div class="container">
                <div class="section-label">Next Steps</div>
                <h2 class="section-title">次のステップ</h2>
                <p class="section-desc">より詳しい機能一覧や内部の仕組み、今後のロードマップについては以下をご覧ください。</p>
                
                <div style="margin-top: 2rem; display: flex; gap: 1rem; flex-wrap: wrap;">
                    <a href="https://github.com/code-fam/unfold#readme" class="btn-ghost" target="_blank" rel="noopener noreferrer">
                        README（詳細マニュアル）を開く
                    </a>
                    <a href="https://marketplace.visualstudio.com/items?itemName=code-fam.unfold" class="btn-primary" target="_blank" rel="noopener noreferrer">
                        VS Code Marketplace で確認する
                    </a>
                </div>
            </div>
        </section>

    </main>
"""

output_html = f"<!DOCTYPE html>\n<html lang=\"ja\">\n{head}\n<body>\n{header}\n{MAIN_CONTENT}\n{footer}\n</body>\n</html>"

with open('quickstart.html', 'w', encoding='utf-8') as f:
    f.write(output_html)

print('Successfully created quickstart.html')
