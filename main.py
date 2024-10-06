import os
import subprocess
import asyncio
import contextlib
import webbrowser
import glob

from src.consts import HOST, PORT, DIR_MODS_ROOT
from src.core import GameMod
from src.exceptions import _BaseHelperException
from src.langs import locale, Langs
from src.log import logger
from src.server import app


# 是否啓用本地服務器測試模組改動，使用此功能需要手動下載好 ModLoader 並如 README 所述把 "Degrees...html" 放到 "modloader" 文件夾中
# Test the mod in local server or not, which needs to download ModLoader manually and place the "Degrees...html" into "modloader" folder
REMOTE_TEST: bool = False
# REMOTE_TEST = True


async def main():
    logger.info("===== ts相關處理開始")
    for dir_path in glob.glob(os.path.join(DIR_MODS_ROOT, "*")):
        abs_path = os.path.abspath(dir_path)  # 獲取絕對路徑
        tsList = glob.glob(os.path.join(abs_path, "**/*.ts"), recursive=True)
        if len(tsList) == 0:
            continue
        else:
            logger.info("   === 發現含有ts檔案的目錄: " + abs_path)
            logger.info("          - ts編譯開始")
            result = subprocess.run(["tsc"], cwd=abs_path,
                                    capture_output=True, text=True, shell=True, encoding='utf-8')
            logger.info("          - ts編譯結束,返回碼為" + str(result.returncode))
    logger.info("##### ts相關處理結束")

    mod = GameMod(REMOTE_TEST)
    mod.build_boot_json()  # For ModLoader
    mod.process_results(auto_apply=False)
    mod.package()


if __name__ == '__main__':
    with contextlib.suppress(_BaseHelperException):
        asyncio.run(main())
        if REMOTE_TEST:
            webbrowser.open(f"http://{HOST}:{PORT}")
            logger.warning(
                locale(Langs.WarningWebBrowserInfo, host=HOST, port=PORT))
            app.run(host=HOST, port=PORT)
