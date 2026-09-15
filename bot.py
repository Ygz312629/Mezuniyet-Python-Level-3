import discord
from discord.ext import commands
from discord.ui import Button, View, Select
import database  # Veri tabanı modülümüzü içe aktarıyoruz

# Veri tabanını ilklendir
database.init_db()

# Bot yapılandırması ve Intent izinleri
intents = discord.Intents.default()
intents.message_content = True  # Metin mesajlarını okuma izni
bot = commands.Bot(command_prefix="!", intents=intents)

# ==========================================
# ETKİLEŞİMLİ BİLEŞENLER (UI / BUTTONS / MENUS)
# ==========================================

# 1. Aşama: Alan Seçim Menüsü (Select Menu)
class FieldSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Teknoloji", description="Yazılım, AI ve Siber Güvenlik alanları"),
            discord.SelectOption(label="Sanat", description="Tasarım, Görsel Sanatlar ve Yaratıcı içerikler"),
            discord.SelectOption(label="Sağlık", description="Biyoloji, Tıp ve Veri Analizi alanları", emoji="🧬")
        ]
        super().__init__(placeholder="İlginizi çeken bir kariyer alanı seçin...", options=options)

    async def callback(self, interaction: discord.Interaction):
        # Kullanıcının seçtiği alanı al
        selected_field = self.values[0]
        careers = database.get_careers_by_field(selected_field)

        # Seçilen alana uygun yanıt oluştur
        embed = discord.Embed(
            title=f"{selected_field} Alanındaki Kariyer Önerileri",
            description="Aşağıda sizin için seçtiğimiz popüler meslekler yer almaktadır:",
            color=discord.Color.blue()
        )

        for title, desc, skills in careers:
            embed.add_field(
                name=f"{title}",
                value=f"**Açıklama:** {desc}\n**Gerekli Yetenekler:** `{skills}`",
                inline=False
            )

        # Yanıtı gönder ve alt kısıma yönlendirme butonu ekle
        view = DetailView()
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

# 2. Aşama: Bilgi ve İletişim Butonları
class DetailView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Detaylı Rehber İste", style=discord.ButtonStyle.primary)
    async def guide_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            "**Kariyer Gelişim Rehberi:** Seçtiğiniz alanda kendinizi geliştirmek için online kurslar (Coursera, Udemy) ve açık kaynaklı projelere katılarak işe başlayabilirsiniz!",
            ephemeral=True
        )

    @discord.ui.button(label="Danışmanla Görüş", style=discord.ButtonStyle.success)
    async def contact_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            "Bir danışmanımız yakında sizinle iletişime geçecek. Sorularınızı direkt bu kanala yazabilirsiniz!",
            ephemeral=True
        )

# Ana Görünüm (Menüyü İhtiva Eden View)
class MainCareerCard(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FieldSelect())

# ==========================================
# BOT OLAYLARI VE KOMUTLARI
# ==========================================

@bot.event
async def on_ready():
    print(f"[{bot.user}] Kariyer Danışmanı Botu başarıyla çevrimiçi oldu!")

# Metin Komutu: Botun ana menüsünü çağırır
@bot.command(name="kariyer")
async def career_command(ctx):
    """Kullanıcıya kariyer seçim kartını ve arayüzünü sunar."""
    embed = discord.Embed(
        title="Geleceğin Kariyerini Keşfet!",
        description="Girişimimize hoş geldiniz! Hayalinizdeki mesleği bulmak için aşağıdaki menüden ilgi duyduğunuz alanı seçin.",
        color=discord.Color.gold()
    )
    embed.set_footer(text="Gelişmiş Kariyer Botu Demo Sürümü v1.0")

    # Arayüzü mesajla birlikte gönder
    await ctx.send(embed=embed, view=MainCareerCard())

# Metin Komutu: Doğrudan arama yapmayı sağlar
@bot.command(name="ara")
async def search_command(ctx, *, alan: str):
    """Kullanıcının doğrudan metin ile arama yapmasını sağlar (Örnek: !ara Teknoloji)"""
    careers = database.get_careers_by_field(alan.capitalize())
    
    if not careers:
        await ctx.send(f"**{alan}** alanına ait bir kariyer bulunamadı. Lütfen `Teknoloji`, `Sanat` veya `Sağlık` şeklinde tekrar deneyin.")
        return

    embed = discord.Embed(
        title=f"'{alan}' Arama Sonuçları",
        color=discord.Color.green()
    )
    for title, desc, skills in careers:
        embed.add_field(name=title, value=f"{desc}\n*Yetenekler:* {skills}", inline=False)
        
    await ctx.send(embed=embed)


# Botu çalıştırın (TOKEN alanına kendi Discord Bot Token'ınızı ekleyin)
bot.run("MTQ1MDUzNDUyNjcyMjc2ODk5Mg.GY6ipw.U1ptTQlf23oux7DA6__lrc46impoiSQKfxDgoE")
