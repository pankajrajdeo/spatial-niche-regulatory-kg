import time, urllib.parse, urllib.request, json

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

PMIDS = """36413377 33385216 28798251 34936882 37516747 37291214 33208946 32996785
32832599 32832598 35078977 31209336 32726565 31949184 31600171 33707239 34927678
33164753 34922464 34030460 39461973 36661515 29236308 39167456 42261399
29087512 32858223 31114921 31340985 37843125 26424082 30445619 36124642 31598675
37956336 35325188 38749504 30462313 34986601 34508353 29069589 25915600 32728249
31680165 39657122 30247620 36914875""".split()

def efetch(pmids):
    url = BASE + "efetch.fcgi?db=pubmed&retmode=xml&rettype=abstract&id=" + ",".join(pmids)
    with urllib.request.urlopen(url) as f:
        return f.read().decode("utf-8", "replace")

out = []
for i in range(0, len(PMIDS), 10):
    out.append(efetch(PMIDS[i:i+10]))
    time.sleep(0.5)

xml = "\n".join(out)
open("/private/tmp/claude-503/-Users-saljh8/86ec3749-a2e6-4d98-b638-3d92bedbda91/scratchpad/abstracts.xml","w").write(xml)

# crude text extraction
import re, html
for art in re.split(r"</PubmedArticle>", xml):
    pm = re.search(r"<PMID[^>]*>(\d+)</PMID>", art)
    ti = re.search(r"<ArticleTitle>(.*?)</ArticleTitle>", art, re.S)
    abs_parts = re.findall(r"<AbstractText[^>]*>(.*?)</AbstractText>", art, re.S)
    if not pm: continue
    clean = lambda s: html.unescape(re.sub(r"<[^>]+>", "", s)).strip()
    print("PMID %s :: %s" % (pm.group(1), clean(ti.group(1)) if ti else ""))
    print("   ABS: %s" % (" ".join(clean(a) for a in abs_parts)[:1400] or "(none)"))
    print()
