from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Autores"


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
    autores = models.ManyToManyField(Autor, related_name="livros")

    def __str__(self):
        return f"{self.titulo} ({self.quantidade}) - {self.preco}"

