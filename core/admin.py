from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import Autor, Categoria, Editora, Livro, Usuario


class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "cpf",
                    "telefone",
                    "data_nascimento",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "email",
    )
    ordering = ("nome",)
    search_fields = ("nome", "email")


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    search_fields = ("descricao",)
    list_filter = ("descricao",)
    ordering = ("descricao",)


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    list_filter = ("nome",)
    ordering = ("nome",)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = (
        "categoria",
        "titulo",
        "editora",
    )
    ordering = ("categoria", "titulo")
    search_fields = (
        "categoria__descricao",
        "titulo",
        "editora__nome",
    )
    list_filter = (
        "categoria",
        "editora",
    )
    list_per_page = 15
