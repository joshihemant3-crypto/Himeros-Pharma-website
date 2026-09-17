import re

def create_blog(template_path, new_file, title, image, category, date, content):
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace Title
    html = re.sub(r'<h1 class="text-3xl lg:text-5xl font-bold text-gray-900 mb-6">.*?</h1>',
                  f'<h1 class="text-3xl lg:text-5xl font-bold text-gray-900 mb-6">{title}</h1>', html, flags=re.DOTALL)
    
    # Replace Image
    html = re.sub(r'<img src="https://picsum\.photos/.*?class="w-full h-full object-cover">',
                  f'<img src="{image}" alt="{title}" class="w-full h-full object-cover">', html)
                  
    # Replace Category & Date
    html = re.sub(r'<span class="text-xs font-semibold text-brand-600 bg-brand-50 px-3 py-1 rounded-full">.*?</span>',
                  f'<span class="text-xs font-semibold text-brand-600 bg-brand-50 px-3 py-1 rounded-full">{category}</span>', html)
    html = re.sub(r'<span class="text-sm font-medium text-gray-500"><i data-lucide="calendar".*?</span>',
                  f'<span class="text-sm font-medium text-gray-500"><i data-lucide="calendar" class="w-4 h-4"></i> {date}</span>', html)

    # Replace Content (everything inside <div class="prose max-w-none text-gray-600 space-y-6"> ... </div>)
    content_match = re.search(r'(<div class="prose max-w-none text-gray-600 space-y-6">)(.*?)(</div>\s*</div>\s*<!-- Sidebar -->)', html, re.DOTALL)
    if content_match:
        html = html.replace(content_match.group(2), f'\n{content}\n')

    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created {new_file}")

template = "blog-isr-2025.html"

# Blog 1
content1 = """
<p class="text-lg leading-relaxed mb-6">Infertility is often viewed through the lens of women's health, but male factors contribute to approximately half of all infertility cases. Understanding the subtle indicators of fertility challenges is the first step toward proactive reproductive health care.</p>
<h3 class="text-2xl font-bold text-gray-900 mt-8 mb-4">1. Changes in Sexual Desire</h3>
<p>A noticeable drop in your sex drive could indicate underlying hormonal issues, particularly low testosterone levels, which directly affect sperm production.</p>
<h3 class="text-2xl font-bold text-gray-900 mt-8 mb-4">2. Testicular Pain or Swelling</h3>
<p>Pain, swelling, or a lump in the testicular area could be a sign of a varicocele (swollen veins) or other conditions that impact fertility.</p>
<h3 class="text-2xl font-bold text-gray-900 mt-8 mb-4">3. Erectile Dysfunction</h3>
<p>Difficulty achieving or maintaining an erection often points to vascular or hormonal imbalances that can also compromise reproductive capability.</p>
<p class="mt-8">If you're experiencing any of these symptoms, early consultation with a healthcare professional can significantly improve outcomes. At Himeros Pharma, we are dedicated to providing science-backed solutions for male reproductive health.</p>
"""
create_blog(template, "blog-male-infertility.html", "Male Infertility: Early Signs Men Should Not Ignore", "https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", "Men's Health", "Oct 12, 2025", content1)

# Blog 2
content2 = """
<p class="text-lg leading-relaxed mb-6">Hypoactive Sexual Desire Disorder (HSDD) and low libido affect both men and women, yet they remain highly stigmatized and misunderstood conditions. Exploring the hidden culprits is the first step to reclaiming your vitality.</p>
<h3 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Hormonal Imbalance</h3>
<p>For men, low testosterone is a primary driver. For women, fluctuations in estrogen and progesterone, especially during menopause, can significantly dampen sexual desire.</p>
<h3 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Chronic Stress and Fatigue</h3>
<p>Elevated cortisol levels from chronic stress suppress sex hormones. Mental exhaustion leaves little energy for intimacy, creating a cycle of frustration.</p>
<h3 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Reclaiming Your Spark</h3>
<p>Addressing low libido involves a holistic approach. Hormonal therapies, stress management techniques, and open communication with your partner are essential. Himeros Pharma provides evidence-based therapies designed to restore neurohormonal balance and enhance quality of life.</p>
"""
create_blog(template, "blog-low-libido.html", "Understanding Low Libido in Men & Women", "https://images.unsplash.com/photo-1518644730709-0835105d9daa?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", "Wellness", "Nov 05, 2025", content2)

# Blog 3
content3 = """
<p class="text-lg leading-relaxed mb-6">When managing Chronic Kidney Disease (CKD), your diet is not just about restrictions—it's a critical tool for slowing disease progression and fueling cellular longevity.</p>
<h3 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Managing Protein Intake</h3>
<p>While protein is essential, processing high amounts of it puts stress on the kidneys. Finding the right balance of high-quality, easily digestible proteins is vital for renal preservation.</p>
<h3 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Sodium, Potassium, and Phosphorus</h3>
<p>Kidneys regulate these minerals. When kidney function declines, these minerals can build up to dangerous levels. Monitoring intake of processed foods, certain fruits, and dairy is key.</p>
<h3 class="text-2xl font-bold text-gray-900 mt-8 mb-4">The Role of Hydration</h3>
<p>Fluid intake recommendations vary wildly depending on the stage of CKD. Working with a nephrologist to determine your specific fluid needs prevents fluid overload and supports remaining kidney function.</p>
<p class="mt-8">Himeros Pharma is committed to advanced renal care therapies that complement lifestyle and nutritional modifications for optimal kidney health.</p>
"""
create_blog(template, "blog-kidney-nutrition.html", "The Role of Nutrition in Kidney Disease Management", "https://images.unsplash.com/photo-1490645935967-10de6ba17061?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", "Nutrition", "Nov 18, 2025", content3)
