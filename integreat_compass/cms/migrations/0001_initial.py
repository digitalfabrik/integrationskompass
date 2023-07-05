# Generated by Django 4.2.1 on 2023-06-11 13:38

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import integreat_compass.cms.models.validators


class Migration(migrations.Migration):
    """
    Add required models
    """

    initial = True

    dependencies = [("auth", "0012_alter_user_first_name_max_length")]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Valid email address for this user",
                        max_length=254,
                        unique=True,
                        verbose_name="email",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        help_text="This name will be shown as the author of votes, comments, etc.",
                        max_length=128,
                        verbose_name="display name",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "ordering": ["email"],
                "default_permissions": ("change", "delete", "view"),
            },
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the responsible contact person",
                        max_length=255,
                        verbose_name="name",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Email address of the responsible contact person",
                        max_length=254,
                        verbose_name="email",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        help_text="Phone number of the responsible contact person",
                        max_length=20,
                        verbose_name="phone number",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "offer contact",
                "verbose_name_plural": "offer contacts",
                "ordering": ["name"],
                "default_permissions": ("change", "delete", "view"),
                "default_related_name": "offer_contact",
            },
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "native_name",
                    models.CharField(
                        help_text="The name of the language in this language",
                        max_length=50,
                        verbose_name="native name",
                    ),
                ),
                (
                    "english_name",
                    models.CharField(
                        help_text="The name of the language in English",
                        max_length=50,
                        verbose_name="name in English",
                    ),
                ),
            ],
            options={
                "verbose_name": "language",
                "verbose_name_plural": "languages",
                "ordering": ["english_name"],
                "default_related_name": "language",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "address",
                    models.TextField(
                        blank=True,
                        help_text="Physical location where the offer takes place",
                        null=True,
                        verbose_name="address",
                    ),
                ),
                (
                    "lat",
                    models.DecimalField(
                        blank=True,
                        decimal_places=7,
                        max_digits=10,
                        null=True,
                        verbose_name="latitude",
                    ),
                ),
                (
                    "long",
                    models.DecimalField(
                        blank=True,
                        decimal_places=7,
                        max_digits=10,
                        null=True,
                        verbose_name="longitude",
                    ),
                ),
            ],
            options={
                "verbose_name": "location",
                "verbose_name_plural": "locations",
                "ordering": ["address"],
                "default_permissions": ("change", "delete", "view"),
                "default_related_name": "location",
            },
        ),
        migrations.CreateModel(
            name="Offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "group_type",
                    models.CharField(
                        choices=[
                            ("PRIVATE", "private"),
                            ("GROUP", "group"),
                            ("BOTH", "both"),
                        ],
                        default="GROUP",
                        help_text="Select in what group sizes lessons are offered",
                        verbose_name="group type",
                    ),
                ),
                (
                    "mode_type",
                    models.CharField(
                        choices=[
                            ("ONLINE", "online"),
                            ("HYBRID", "hybrid"),
                            ("IN_PERSON", "in person"),
                        ],
                        default="IN_PERSON",
                        help_text="Select in what mode lessons are offered",
                        verbose_name="lesson mode",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cms.location"
                    ),
                ),
                (
                    "offer_contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cms.contact"
                    ),
                ),
            ],
            options={"verbose_name": "offer", "verbose_name_plural": "offers"},
        ),
        migrations.CreateModel(
            name="OfferVersion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "offer_version_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Title of this offer",
                        max_length=255,
                        verbose_name="title",
                    ),
                ),
                (
                    "title_image",
                    models.ImageField(
                        blank=True,
                        default="fallback_title_image.png",
                        help_text="Choose a title image for this offer",
                        upload_to="images/",
                        validators=[
                            integreat_compass.cms.models.validators.file_size_limit
                        ],
                        verbose_name="title image",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Detailed information about the offer",
                        verbose_name="description",
                    ),
                ),
                (
                    "is_free",
                    models.BooleanField(
                        default=True,
                        help_text="Whether this offer is free or not",
                        verbose_name="Free offer",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        default=integreat_compass.cms.models.offers.offer_version.get_default_language,
                        help_text="The language being taught in this offer",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cms.language",
                        verbose_name="Language",
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="cms.offer",
                    ),
                ),
            ],
            options={
                "verbose_name": "offer version",
                "verbose_name_plural": "offer versions",
                "ordering": ["-offer_version_date"],
                "default_related_name": "offer_versions",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Title of the tag", max_length=32, verbose_name="tag"
                    ),
                ),
            ],
            options={
                "verbose_name": "tag",
                "verbose_name_plural": "tags",
                "ordering": ["title"],
                "default_related_name": "tag",
            },
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        help_text="Reason for the report", verbose_name="comment"
                    ),
                ),
                (
                    "offer_version",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cms.offerversion",
                    ),
                ),
            ],
            options={
                "verbose_name": "report",
                "verbose_name_plural": "reports",
                "default_permissions": ("add", "view"),
                "default_related_name": "reports",
            },
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the organization",
                        max_length=255,
                        verbose_name="organization name",
                    ),
                ),
                (
                    "web_address",
                    models.URLField(
                        help_text="URL of the website or social media of the organization",
                        verbose_name="website",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "organization",
                "verbose_name_plural": "organizations",
                "ordering": ["name"],
                "default_permissions": ("change", "delete", "view"),
                "default_related_name": "organization",
            },
        ),
        migrations.AddField(
            model_name="offer",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cms.organization"
            ),
        ),
        migrations.AddField(
            model_name="offer",
            name="tags",
            field=models.ManyToManyField(blank=True, to="cms.tag"),
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="documents/",
                        validators=[
                            integreat_compass.cms.models.validators.file_size_limit
                        ],
                        verbose_name="file",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("file_size", models.IntegerField(verbose_name="file size")),
                (
                    "file_type",
                    models.CharField(
                        choices=[
                            ("image/png", "PNG image"),
                            ("image/jpeg", "JPEG image"),
                            ("application/pdf", "PDF document"),
                        ],
                        max_length=128,
                        verbose_name="file type",
                    ),
                ),
                ("offer_versions", models.ManyToManyField(to="cms.offerversion")),
            ],
            options={
                "verbose_name": "document",
                "verbose_name_plural": "documents",
                "ordering": ["name"],
                "default_permissions": ("add", "delete", "view"),
                "default_related_name": "documents",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "comment",
                    models.TextField(
                        help_text="Additional context for the given rating",
                        verbose_name="comment",
                    ),
                ),
                (
                    "rating",
                    models.PositiveSmallIntegerField(
                        help_text="Rating of the offer",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="rating",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "offer_version",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cms.offerversion",
                    ),
                ),
            ],
            options={
                "verbose_name": "comment",
                "verbose_name_plural": "comments",
                "ordering": ["date"],
                "default_permissions": ("add", "delete", "view"),
                "default_related_name": "comments",
            },
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "approval",
                    models.BooleanField(
                        help_text="Whether the vote approves or disapproves of an offer",
                        verbose_name="approval",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        help_text="Reason for approving or disapproving an offer",
                        verbose_name="comment",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "offer_version",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cms.offerversion",
                    ),
                ),
            ],
            options={
                "verbose_name": "vote",
                "verbose_name_plural": "votes",
                "default_permissions": ("add", "view"),
                "default_related_name": "votes",
                "unique_together": {("creator", "offer_version")},
            },
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cms.offer"
                    ),
                ),
            ],
            options={
                "verbose_name": "favorite",
                "verbose_name_plural": "favorites",
                "default_permissions": ("add", "delete", "view"),
                "default_related_name": "favorite",
                "unique_together": {("creator", "offer")},
            },
        ),
    ]
