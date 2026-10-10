BLITZ_CSS='''<style>
.reveal .slides section .fragment.blitz{opacity:1;visibility:inherit;transition:none;transform:none;padding:0;margin:0;position:fixed;inset:0;width:100% !important;max-width:none !important;display:flex;align-items:center;justify-content:center;pointer-events:none;}
.reveal .slides section .fragment.blitz img{opacity:0;height:92%;width:auto;max-width:96%;margin:0;box-shadow:0 0 1.5rem rgba(0,0,0,.25);}
.reveal .slides section .fragment.blitz.visible img{animation:blitz-zeigen var(--dauer,50ms) linear 1;}
@keyframes blitz-zeigen{from{opacity:1}to{opacity:1}}
</style>'''
def blitz(img, titel, frage, dauer='50ms', alt='Screenshot einer Website', css=False):
    return f'''<section class="simple" data-transition="none">
  <div>
    <h1>{titel}</h1>
    <p>{frage}</p>
    <div class="fragment blitz" style="--dauer:{dauer};"><img src="{img}" alt="{alt}"></div>{BLITZ_CSS if css else ''}
  </div>
</section>
'''
