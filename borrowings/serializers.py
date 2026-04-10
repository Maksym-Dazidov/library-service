from rest_framework import serializers

from borrowings.models import Borrowing
from books import Book

class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ('book_id', 'user_id', 'borrow_date')


class BorrowingDetailSerializer(BorrowingSerializer):
    class Meta:
        fields = ('book_id', 'user_id', 'borrow_date', 'expected_return_date', 'actual_return_date')

class BorrowingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ['book_id', 'expected_return_date']

    def validate(self, data):
        book = Book.objects.get(pk=data['book_id'])

        if book.inventory <= 0:
            raise serializers.ValidationError('Book is not available')

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        book = Book.objects.get(pk=validated_data['book_id'])

        book.inventory -= 1
        book.save()

        borrowing = Borrowing.objects.create(
            user=user,
            **validated_data
        )
        return borrowing
