#!/usr/bin/python3
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Tests the HBNBCommand console."""

    def setUp(self):
        """Setup the environment for each test."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after each test."""
        storage._FileStorage__objects.clear()

    def test_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(output.getvalue().strip(), "Exiting...")

    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(output.getvalue().strip(), "")

    def test_emptyline(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(self.console.onecmd(""))
            self.assertEqual(output.getvalue().strip(), "")

    def test_default(self):
        """Test unknown command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("unknowncommand")
            self.assertIn(
                "*** Unknown command: unknowncommand",
                output.getvalue().strip()
            )

    def test_create(self):
        """Test create command with and without arguments."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create")
            self.assertEqual(
                output.getvalue().strip(),
                "** class name missing **"
            )

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create MyModel")
            self.assertEqual(
                output.getvalue().strip(),
                "** class doesn't exist **"
            )

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            self.assertIn("BaseModel.", output.getvalue().strip())

    def test_show(self):
        """Test show command with various scenarios."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("show")
            self.assertEqual(
                output.getvalue().strip(),
                "** class name missing **"
            )

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("show MyModel")
            self.assertEqual(
                output.getvalue().strip(),
                "** class doesn't exist **"
            )

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("show BaseModel")
            self.assertEqual(
                output.getvalue().strip(),
                "** instance id missing **"
            )

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("show BaseModel 12345")
            self.assertEqual(
                output.getvalue().strip(),
                "** no instance found **"
            )

        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd(f"show BaseModel {obj.id}")
            self.assertIn(
                f"[BaseModel] ({obj.id})",
                output.getvalue().strip()
            )


if __name__ == '__main__':
    unittest.main()
