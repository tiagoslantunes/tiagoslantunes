import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")


class ProfileReadmeTests(unittest.TestCase):
    def test_all_portfolio_repositories_are_linked(self):
        expected = {
            "text-mining-financial-sentiment",
            "cifo-ga-image-reconstruction",
            "Car-price-prediction-ml",
            "novatrade-database",
            "Streamlining-Data-Reporting-Processes",
            "fund-analytics-pipelines",
            "r-outlook-alerts-template",
            "Yahtzee",
        }
        for repository in expected:
            with self.subTest(repository=repository):
                self.assertIn(f"github.com/tiagoslantunes/{repository}", README)

    def test_local_images_exist(self):
        sources = re.findall(r'src="([^"/][^"]*)"', README)
        local_sources = [src for src in sources if not src.startswith(("http://", "https://"))]
        for source in local_sources:
            with self.subTest(source=source):
                self.assertTrue((ROOT / source).is_file())


if __name__ == "__main__":
    unittest.main()
