import re

# Read the original segment.html to keep the header, nav, and footer
with open('segment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract everything before <!-- Segment Section -->
header_match = re.search(r'(.*?)<!-- Segment Section -->', content, re.DOTALL)
header = header_match.group(1)

# Extract everything after <!-- Footer -->
footer_match = re.search(r'(<!-- Footer -->.*)', content, re.DOTALL)
footer = footer_match.group(1)

# Build the new content
new_content = """
    <!-- Page Header -->
    <section class="relative pt-32 pb-20 lg:pt-40 lg:pb-28 bg-brand-900 overflow-hidden">
        <div class="absolute inset-0 z-0">
            <img src="assets/sources/aboutus.jpg" alt="Therapies Background" class="w-full h-full object-cover opacity-20">
            <div class="absolute inset-0 bg-gradient-to-b from-brand-900/90 to-brand-900"></div>
        </div>
        <div class="relative z-10 max-w-7xl mx-auto px-4 text-center">
            <div class="inline-flex items-center gap-2 mb-4 justify-center">
                <div class="w-8 h-0.5 bg-brand-400"></div>
                <span class="text-xs font-semibold text-brand-300 uppercase tracking-widest">Our Expertise</span>
                <div class="w-8 h-0.5 bg-brand-400"></div>
            </div>
            <h1 class="text-4xl lg:text-6xl font-bold text-white mb-6">Our Therapies</h1>
            <p class="text-lg text-brand-100 max-w-2xl mx-auto leading-relaxed">Delivering specialized healthcare solutions across key therapeutic areas to improve quality of life for millions.</p>
        </div>
    </section>

    <!-- Andrology/Sexology/Urology Section -->
    <section class="py-20 lg:py-28 bg-white">
        <div class="max-w-7xl mx-auto px-4">
            <div class="text-center mb-16">
                <h2 class="text-3xl lg:text-4xl font-bold text-brand-600 mb-6">Andrology / Sexology / Urology</h2>
                <div class="max-w-4xl mx-auto text-left space-y-6 text-gray-600 leading-relaxed">
                    <p>Sexual and reproductive health disorders are increasingly becoming a significant yet under-addressed health concern worldwide. Factors such as hormonal imbalance, metabolic dysfunction, stress, sedentary lifestyles, vascular impairment, delayed parenthood, and chronic conditions are contributing to rising cases of infertility, low libido, erectile dysfunction, menstrual irregularities, and compromised reproductive wellness in both men and women. Beyond physical symptoms, these conditions often affect emotional health, confidence, relationships, and overall quality of life.</p>
                    <p>At Himeros Pharma, we approach andrology and sexual wellness through a science-driven, patient-centric framework focused on restoring physiological balance and supporting long-term reproductive health. Our therapies are developed to address key underlying mechanisms involved in sexual dysfunction and fertility challenges, including endothelial dysfunction, oxidative stress, hormonal dysregulation, impaired nitric oxide signaling, inflammation, and reduced metabolic efficiency.</p>
                    <p>With a focus on safety, tolerability, and sustained outcomes, Himeros Pharma works toward supporting healthy sexual function, reproductive vitality, hormonal equilibrium, and fertility potential in both men and women. By combining clinical insight with evolving therapeutic innovation, we aim to enable comprehensive care solutions that improve not only reproductive outcomes, but also overall health, confidence, and well-being.</p>
                </div>
            </div>

            <!-- Male Sexual Dysfunction -->
            <div class="mb-20">
                <div class="bg-gray-50 rounded-3xl p-8 lg:p-12 border border-gray-100">
                    <h3 class="text-2xl font-bold text-brand-600 mb-4">Male Sexual Dysfunction</h3>
                    <p class="text-gray-600 mb-4 leading-relaxed">Male sexual dysfunction refers to a group of conditions that affect a man's ability to experience satisfactory sexual performance, desire, ejaculation. It is a multifactorial condition influenced by hormonal, vascular, neurological, psychological, metabolic, and lifestyle-related factors.</p>
                    <p class="text-gray-600 mb-8 leading-relaxed">Several underlying mechanisms contribute to male sexual dysfunction, including impaired nitric oxide signaling, poor blood circulation, endothelial dysfunction, testosterone imbalance, oxidative stress, inflammation, diabetes, obesity, chronic kidney disease, stress, anxiety, and unhealthy lifestyle habits such as smoking, alcohol use, and physical inactivity. These conditions not only impact sexual health but can also affect emotional well-being, confidence, relationships, and overall quality of life.</p>
                    
                    <h4 class="text-xl font-bold text-brand-700 mb-6">Our Approach to Sexual Wellness</h4>
                    <p class="text-gray-600 mb-8 leading-relaxed">At Himeros Pharma, sexual wellness is approached as an essential component of overall physical, emotional, and relationship well-being. We understand that concerns such as erectile dysfunction, low libido, performance anxiety, hormonal imbalance, and sexual dissatisfaction are often multifactorial and require a compassionate, science-driven approach. Our focus is on supporting healthy sexual function through clinically informed therapies designed for long-term well-being, confidence, and quality of life.</p>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">01 Patient-Centric Understanding</div>
                            <p class="text-gray-500 text-sm">We recognise that sexual wellness concerns are deeply personal and influenced by vascular health, hormonal balance, stress, lifestyle, and emotional factors. Our approach focuses on addressing these interconnected causes responsibly.</p>
                        </div>
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">02 Science-Led Therapeutic Support</div>
                            <p class="text-gray-500 text-sm">Our formulations are developed to support physiological mechanisms involved in sexual health, including nitric oxide pathways, endothelial function, hormonal regulation, energy metabolism, and overall vitality.</p>
                        </div>
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">03 Long-Term Safety & Wellness</div>
                            <p class="text-gray-500 text-sm">We prioritise therapies designed for tolerability, consistency, and sustained support, recognising that sexual wellness management often requires continuous care and lifestyle alignment.</p>
                        </div>
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">04 Ethical & Stigma-Free Care</div>
                            <p class="text-gray-500 text-sm">Himeros Pharma is committed to promoting awareness, encouraging open conversations, and supporting sexual wellness with dignity, scientific integrity, and patient trust.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Male Infertility -->
            <div class="mb-20">
                <div class="bg-white rounded-3xl p-8 lg:p-12 border border-brand-100 shadow-md">
                    <h3 class="text-2xl font-bold text-brand-600 mb-6">Male Infertility</h3>
                    <h4 class="text-xl font-bold text-brand-700 mb-4">Our Approach to Reproductive Wellness</h4>
                    <p class="text-gray-600 mb-8 leading-relaxed">At Himeros Pharma, reproductive wellness is guided by a commitment to supporting fertility, hormonal health, and reproductive balance in both men and women. We recognise that reproductive challenges are influenced by complex physiological, metabolic, and lifestyle-related factors that require a comprehensive and evidence-based approach. Our therapies are developed to support reproductive health with a focus on long-term outcomes, safety, and holistic well-being.</p>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">01 Fertility-Focused Scientific Approach</div>
                            <p class="text-gray-500 text-sm">Our solutions are designed with an understanding of key reproductive mechanisms including hormonal regulation, gamete health, oxidative stress reduction, metabolic balance, and reproductive system support.</p>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">02 Holistic Reproductive Health Support</div>
                            <p class="text-gray-500 text-sm">We focus on supporting overall reproductive wellness by addressing interconnected factors such as nutrition, stress, endocrine balance, lifestyle habits, and metabolic health.</p>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">03 Quality, Safety & Clinical Responsibility</div>
                            <p class="text-gray-500 text-sm">Our formulations are developed with an emphasis on scientific validation, safety, tolerability, and responsible long-term support for reproductive care journeys.</p>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">04 Empowering Awareness & Early Care</div>
                            <p class="text-gray-500 text-sm">We believe better reproductive outcomes begin with awareness and timely intervention. Himeros Pharma aims to encourage informed healthcare decisions through ethical practices, education, and patient-focused care.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ED / PE / Hypogonadism -->
            <div class="mb-20">
                <div class="bg-gray-50 rounded-3xl p-8 lg:p-12 border border-gray-100">
                    <h3 class="text-2xl font-bold text-brand-600 mb-8">Premature Ejaculation / Erectile Dysfunction / Hypogonadism</h3>
                    
                    <h4 class="text-lg font-bold text-brand-600 mb-2">Erectile Dysfunction (ED)</h4>
                    <p class="text-gray-600 mb-6 leading-relaxed">Erectile dysfunction is the persistent inability to achieve or maintain an erection sufficient for satisfactory sexual performance. It commonly occurs due to impaired nitric oxide signaling, endothelial dysfunction, reduced penile blood flow, hormonal imbalance, diabetes, obesity, cardiovascular disease, stress, anxiety, or neurological disorders. Poor vascular relaxation limits adequate blood filling of the penile tissues, affecting erection quality and rigidity. Common symptoms include difficulty achieving erections, reduced erection firmness, inability to sustain erections during intercourse, reduced sexual confidence, and decreased libido. ED is often associated with underlying metabolic or cardiovascular health disturbances and may significantly impact emotional well-being and relationship health.</p>
                    
                    <h4 class="text-lg font-bold text-brand-600 mb-2">Premature Ejaculation (PE)</h4>
                    <p class="text-gray-600 mb-6 leading-relaxed">Premature ejaculation is a sexual dysfunction characterized by ejaculation occurring earlier than desired, often with minimal sexual stimulation and reduced voluntary control. It is associated with altered serotonin neurotransmission, penile hypersensitivity, psychological stress, anxiety, hormonal imbalance, and sometimes erectile dysfunction itself. Neurobiological factors affecting ejaculatory reflex pathways can lead to rapid climax and reduced ejaculatory latency time. Common symptoms include inability to delay ejaculation, distress during sexual activity, reduced sexual satisfaction, performance anxiety, frustration, and relationship difficulties. The condition can become cyclical, where anxiety and fear of poor performance further worsen ejaculatory control over time.</p>
                    
                    <h4 class="text-lg font-bold text-brand-600 mb-2">Hypogonadism</h4>
                    <p class="text-gray-600 mb-8 leading-relaxed">Hypogonadism is a condition characterized by reduced testosterone production due to dysfunction of the testes or impaired hypothalamic-pituitary hormonal signaling. Testosterone deficiency can result from aging, obesity, diabetes, chronic illness, stress, metabolic disorders, medications, or primary testicular dysfunction. Reduced androgen levels affect sexual, reproductive, metabolic, and musculoskeletal functions. Common symptoms include low libido, fatigue, erectile dysfunction, reduced muscle mass and strength, mood changes, decreased energy, poor concentration, infertility, and reduced sperm production. Long-term hypogonadism may also contribute to metabolic imbalance, reduced bone density, and decline in overall physical and emotional well-being.</p>
                    
                    <h4 class="text-xl font-bold text-brand-700 mb-6">Our Approach</h4>
                    <p class="text-gray-600 mb-8 leading-relaxed">At Himeros Pharma, conditions such as erectile dysfunction, premature ejaculation, and hypogonadism are approached as interconnected health concerns influenced by vascular health, hormonal balance, neurological pathways, metabolic function, and psychological well-being. We recognise that these conditions often coexist and collectively impact sexual performance, confidence, fertility potential, emotional health, and overall quality of life. Our focus is on delivering science-driven, patient-centric solutions that support long-term physiological restoration rather than temporary symptomatic relief.</p>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">01 Multi-Mechanistic Therapeutic Approach</div>
                            <p class="text-gray-500 text-sm">Our therapies are designed to support nitric oxide signaling, endothelial function, neurotransmitter balance, testosterone regulation, energy metabolism, and reproductive health pathways involved in male sexual wellness.</p>
                        </div>
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">02 Root-Cause Oriented Care Philosophy</div>
                            <p class="text-gray-500 text-sm">We focus on addressing contributing factors such as oxidative stress, hormonal imbalance, stress, metabolic dysfunction, lifestyle influences, and vascular impairment through comprehensive care strategies.</p>
                        </div>
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">03 Long-Term Safety & Sustained Wellness</div>
                            <p class="text-gray-500 text-sm">Recognising the chronic and sensitive nature of these conditions, we prioritise formulations developed for safety, tolerability, patient comfort, and long-term adherence.</p>
                        </div>
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">04 Ethical, Patient-Centric & Stigma-Free Care</div>
                            <p class="text-gray-500 text-sm">Himeros Pharma is committed to encouraging awareness, enabling open conversations around men's health, and delivering responsible, evidence-based therapies rooted in trust, dignity, and scientific integrity.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- BPH / LUTS -->
            <div class="mb-20">
                <div class="bg-white rounded-3xl p-8 lg:p-12 border border-brand-100 shadow-md">
                    <h3 class="text-2xl font-bold text-brand-600 mb-8">Benign Prostatic Hyperplasia (BPH) / Lower Urinary Tract Symptoms (LUTS)</h3>
                    
                    <h4 class="text-lg font-bold text-brand-600 mb-2">Benign Prostatic Hyperplasia (BPH)</h4>
                    <p class="text-gray-600 mb-6 leading-relaxed">Benign Prostatic Hyperplasia (BPH) is a progressive, non-cancerous enlargement of the prostate gland that commonly occurs with aging. The condition develops due to hormonal changes, particularly alterations in testosterone and dihydrotestosterone (DHT) activity, leading to increased prostate tissue growth. As the enlarged prostate compresses the urethra, it obstructs urinary flow and contributes to various urinary symptoms. Common manifestations include increased urinary frequency, nocturia (night-time urination), urgency, weak urinary stream, hesitancy, incomplete bladder emptying, and post-void dribbling. If left unmanaged, BPH may significantly impact quality of life and increase the risk of urinary retention and bladder complications.</p>
                    
                    <h4 class="text-lg font-bold text-brand-600 mb-2">Lower Urinary Tract Symptoms (LUTS)</h4>
                    <p class="text-gray-600 mb-6 leading-relaxed">Lower Urinary Tract Symptoms (LUTS) refer to a group of urinary symptoms involving bladder storage, voiding, and post-micturition disturbances. LUTS commonly occur due to BPH but may also result from bladder dysfunction, aging-related changes, inflammation, neurological disorders, metabolic conditions, or urinary tract abnormalities. Storage symptoms include increased urinary frequency, urgency, and nocturia, while voiding symptoms include weak urinary stream, hesitancy, straining, and prolonged urination. Post-micturition symptoms often include a sensation of incomplete bladder emptying and post-void dribbling. These symptoms can adversely affect sleep quality, daily activities, emotional well-being, and overall quality of life.</p>
                    
                    <h4 class="text-xl font-bold text-brand-700 mb-6">Our Approach to BPH & LUTS</h4>
                    <p class="text-gray-600 mb-8 leading-relaxed">At Himeros Pharma, Benign Prostatic Hyperplasia (BPH) and Lower Urinary Tract Symptoms (LUTS) are approached as progressive urological conditions that affect urinary function, sleep quality, daily productivity, and overall well-being. We recognise that these conditions often involve complex interactions between hormonal changes, prostate enlargement, bladder dysfunction, inflammation, and age-related physiological changes. Our focus is on delivering science-driven, patient-centric solutions that support symptom relief, urinary comfort, and long-term prostate health.</p>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">01 Comprehensive Prostate Health Support</div>
                            <p class="text-gray-500 text-sm">Our therapies are designed to support healthy urinary flow, bladder function, prostate health, and symptom management through targeted and evidence-based therapeutic approaches.</p>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">02 Addressing Underlying Contributing Factors</div>
                            <p class="text-gray-500 text-sm">We focus on factors such as hormonal influences, inflammation, oxidative stress, age-related prostate changes, and bladder dysfunction that contribute to disease progression and urinary symptoms.</p>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">03 Long-Term Quality of Life Improvement</div>
                            <p class="text-gray-500 text-sm">Recognising the chronic nature of BPH and LUTS, we prioritise therapies that support sustained symptom control, treatment adherence, patient comfort, and improved daily functioning.</p>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">04 Responsible & Patient-Centric Urological Care</div>
                            <p class="text-gray-500 text-sm">Himeros Pharma is committed to improving awareness, encouraging timely intervention, and providing reliable, scientifically validated solutions that help patients maintain urinary health, confidence, and overall quality of life.</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- HSDD -->
            <div class="mb-10">
                <div class="bg-gray-50 rounded-3xl p-8 lg:p-12 border border-gray-100">
                    <h3 class="text-2xl font-bold text-brand-600 mb-6">Hypoactive Sexual Desire Disorder (HSDD)</h3>
                    <p class="text-gray-600 mb-4 leading-relaxed">Hypoactive Sexual Desire Disorder (HSDD) is a condition characterized by a persistent or recurrent deficiency of sexual thoughts, fantasies, interest, or desire for sexual activity that causes personal distress or interpersonal difficulties. It is a multifactorial disorder influenced by hormonal changes, neurotransmitter imbalance, psychological stress, relationship factors, chronic medical conditions, medications, and lifestyle influences. In women, HSDD is often associated with estrogen deficiency, androgen imbalance, menopause, PCOS, postpartum changes, or emotional stress, while in men it may be linked to testosterone deficiency, metabolic disorders, and chronic illness.</p>
                    <p class="text-gray-600 mb-8 leading-relaxed">Common symptoms include reduced sexual interest, diminished sexual thoughts or fantasies, decreased responsiveness to sexual stimulation, reduced intimacy, loss of motivation for sexual activity, emotional distress, relationship challenges, and a decline in overall quality of life. The condition often affects emotional well-being, self-confidence, and interpersonal relationships, making timely recognition and comprehensive management essential.</p>
                    
                    <h4 class="text-xl font-bold text-brand-700 mb-6">Our Approach to HSDD</h4>
                    <p class="text-gray-600 mb-8 leading-relaxed">At Himeros Pharma, Hypoactive Sexual Desire Disorder is approached as a complex neurohormonal and psychosocial condition that extends beyond sexual desire alone. We recognize that healthy sexual function is influenced by hormonal balance, vascular health, neurotransmitter activity, emotional well-being, and overall vitality. Our focus is on delivering science-driven, patient-centric solutions that support long-term sexual wellness and quality of life.</p>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">01 Supporting Neurohormonal Balance</div>
                            <p class="text-gray-500 text-sm">Our therapies are designed to support the physiological pathways involved in sexual desire, including hormonal regulation, neurotransmitter activity, vascular responsiveness, and energy metabolism.</p>
                        </div>
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">02 Addressing Multifactorial Contributors</div>
                            <p class="text-gray-500 text-sm">We focus on factors such as hormonal imbalance, stress, fatigue, metabolic dysfunction, aging-related changes, and emotional well-being that may contribute to reduced sexual desire and arousal.</p>
                        </div>
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">03 Enhancing Intimacy & Quality of Life</div>
                            <p class="text-gray-500 text-sm">Recognising the impact of HSDD on confidence, relationships, and emotional health, our approach aims to support overall sexual satisfaction, intimacy, and personal well-being.</p>
                        </div>
                        <div class="bg-white p-6 rounded-2xl shadow-sm">
                            <div class="text-brand-600 font-bold mb-2">04 Ethical, Compassionate & Evidence-Based Care</div>
                            <p class="text-gray-500 text-sm">Himeros Pharma is committed to promoting awareness, reducing stigma surrounding sexual wellness concerns, and providing responsible, scientifically validated solutions that support healthier and more fulfilling lives.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Nephrology Section -->
    <section class="py-20 lg:py-28 bg-gradient-to-b from-gray-50 to-white border-t border-gray-100">
        <div class="max-w-7xl mx-auto px-4">
            <div class="text-center mb-16">
                <h2 class="text-3xl lg:text-4xl font-bold text-brand-600 mb-6">Nephrology</h2>
                <div class="max-w-4xl mx-auto text-left space-y-6 text-gray-600 leading-relaxed">
                    <p>At Himeros Pharma, kidney disorders are approached as complex systemic conditions influenced by metabolic dysfunction, inflammation, oxidative stress, cardiovascular health, and nutritional status. We recognise that CKD, DKD, albuminuria, and kidney stone disease often coexist and progressively impact overall health and quality of life. Our focus is on delivering science-driven, patient-centric solutions that support renal preservation, metabolic balance, and long-term disease management.</p>
                </div>
            </div>

            <div class="mb-16">
                <div class="bg-white rounded-3xl p-8 lg:p-12 border border-brand-100 shadow-md">
                    <h3 class="text-2xl font-bold text-brand-600 mb-8">Chronic Kidney Disease / Diabetic Kidney Disease / Albuminuria / Kidney Stones</h3>
                    
                    <h4 class="text-lg font-bold text-brand-600 mb-2">Chronic Kidney Disease (CKD)</h4>
                    <p class="text-gray-600 mb-6 leading-relaxed">Chronic Kidney Disease (CKD) is a progressive condition characterized by gradual and irreversible loss of kidney function over time. As kidney function declines, the body's ability to eliminate metabolic waste, regulate fluid and electrolyte balance, and maintain hormonal homeostasis becomes impaired. CKD commonly develops due to diabetes, hypertension, recurrent infections, glomerular disorders, kidney stones, and chronic inflammation. Common symptoms include fatigue, swelling, loss of appetite, nocturia, foamy urine, hypertension, and declining renal function. Without timely intervention, CKD may progress to end-stage kidney disease requiring dialysis or transplantation.</p>
                    
                    <h4 class="text-lg font-bold text-brand-600 mb-2">Diabetic Kidney Disease (DKD)</h4>
                    <p class="text-gray-600 mb-6 leading-relaxed">Diabetic Kidney Disease (DKD) is a major complication of diabetes resulting from chronic hyperglycemia-induced damage to renal microvasculature and glomerular structures. Persistent metabolic stress triggers inflammation, oxidative damage, protein leakage, and progressive nephron loss. Early disease may remain asymptomatic, while advancing stages are associated with albuminuria, declining GFR, edema, hypertension, and increased cardiovascular risk. DKD remains one of the leading causes of chronic kidney failure globally.</p>
                    
                    <h4 class="text-lg font-bold text-brand-600 mb-2">Albuminuria</h4>
                    <p class="text-gray-600 mb-6 leading-relaxed">Albuminuria refers to the abnormal leakage of albumin into the urine and is often one of the earliest indicators of kidney damage. It occurs due to increased permeability of the glomerular filtration barrier and is commonly associated with diabetes, hypertension, inflammation, and chronic kidney disease. Persistent albuminuria is not only a marker of renal injury but also a predictor of cardiovascular complications and progressive loss of kidney function.</p>

                    <h4 class="text-lg font-bold text-brand-600 mb-2">Kidney Stones (Nephrolithiasis)</h4>
                    <p class="text-gray-600 mb-8 leading-relaxed">Kidney stones are hard mineral deposits that form within the kidneys due to abnormalities in urine composition, hydration status, metabolic disturbances, or recurrent infections. Patients may experience severe flank pain, blood in urine, urinary obstruction, recurrent infections, and renal tissue injury. Recurrent stone disease can contribute to chronic inflammation, kidney damage, and long-term decline in renal function if not adequately managed.</p>
                    
                    <h4 class="text-xl font-bold text-brand-700 mb-6">Our Approach to Renal Health</h4>
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">01 Preserving Renal Function & Slowing Disease Progression</div>
                            <p class="text-gray-500 text-sm">Our therapies are designed to support nephron preservation, reduce protein loss, maintain metabolic balance, and help slow the progression of kidney impairment across various stages of renal disease.</p>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">02 Addressing Oxidative Stress & Inflammation</div>
                            <p class="text-gray-500 text-sm">We focus on key pathological drivers including oxidative stress, chronic inflammation, endothelial dysfunction, toxin accumulation, and metabolic disturbances that contribute to ongoing renal injury and disease progression.</p>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">03 Comprehensive Management of Renal Complications</div>
                            <p class="text-gray-500 text-sm">Our approach supports patients facing albuminuria, diabetic kidney damage, kidney stone recurrence, electrolyte imbalance, nutritional deficiencies, and associated cardiovascular risks through integrated therapeutic strategies.</p>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-2xl">
                            <div class="text-brand-600 font-bold mb-2">04 Long-Term Patient Well-Being & Quality of Life</div>
                            <p class="text-gray-500 text-sm">Recognising the lifelong nature of many kidney disorders, we prioritise therapies that support treatment adherence, nutritional health, symptom control, and sustainable long-term outcomes while empowering patients and healthcare professionals through evidence-based renal care.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

with open('segment.html', 'w', encoding='utf-8') as f:
    f.write(header + new_content + footer)

print("Updated segment.html successfully.")
