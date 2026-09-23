#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════╗
║   Zain Iraq Bot v8.0 — Telebot Edition                  ║
║   حقوق التطوير: @to_ls                                   ║
╚══════════════════════════════════════════════════════════╝
"""

import re
import json
import base64
import time
import logging
import requests
from datetime import datetime
import telebot
from telebot import types


# ═══════════════════════════════════════════════════════════
#                    الإعدادات
# ═══════════════════════════════════════════════════════════
BOT_TOKEN = "8649116276:AAGRor3c0juxDASZ2tJPutf31nGbXQ2NsSg"

DEVELOPER = "@to_ls"
DEV_LINK = "https://t.me/to_ls"
CHANNEL_LINK = "https://t.me/to_ls"

BASE_URL = "https://mw-mobileapp.iq.zain.com/api"

COMMON_HEADERS = {
    'User-Agent': "okhttp/4.11.0",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Skel-Accept-Language': "ar",
    'Skel-Platform': "Android",
    'Skel-OS-Version': "15",
    'Skel-Fix-Version': "6.5.0",
    'Skel-Installation-Id': "a7f6551e0ac34017fcf8c1cf7ac56bada3eb793b",
    'Content-Type': "application/json; charset=UTF-8"
}


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════════════════════
#                    إنشاء البوت
# ═══════════════════════════════════════════════════════════
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

USER_STATE = {}
CACHE = {}


# ═══════════════════════════════════════════════════════════
#     🎨 الإيموجيات المميزة
# ═══════════════════════════════════════════════════════════
_CE = {
    '👑': '<tg-emoji emoji-id="5319149831673887746">👑</tg-emoji>',
    '⭐': '<tg-emoji emoji-id="5254001839287859496">⭐</tg-emoji>',
    '💎': '<tg-emoji emoji-id="5254001839287859496">💎</tg-emoji>',
    '✨': '<tg-emoji emoji-id="5254001839287859496">✨</tg-emoji>',
    '🎉': '<tg-emoji emoji-id="5254001839287859496">🎉</tg-emoji>',
    '🎨': '<tg-emoji emoji-id="5254001839287859496">🎨</tg-emoji>',
    '🤖': '<tg-emoji emoji-id="5254001839287859496">🤖</tg-emoji>',
    '😎': '<tg-emoji emoji-id="5976308930660276596">😎</tg-emoji>',
    '👋': '<tg-emoji emoji-id="5319149831673887746">👋</tg-emoji>',
    '🧙': '<tg-emoji emoji-id="5803157577525106419">🧙</tg-emoji>',
    '💰': '<tg-emoji emoji-id="6037182124916740433">💰</tg-emoji>',
    '💵': '<tg-emoji emoji-id="6003691769533829755">💵</tg-emoji>',
    '💳': '<tg-emoji emoji-id="5447453226498552490">💳</tg-emoji>',
    '💲': '<tg-emoji emoji-id="6003691769533829755">💲</tg-emoji>',
    '💗': '<tg-emoji emoji-id="6043941205144771802">💗</tg-emoji>',
    '👤': '<tg-emoji emoji-id="5373020661574826232">👤</tg-emoji>',
    '👥': '<tg-emoji emoji-id="6001388309853510348">👥</tg-emoji>',
    '👁': '<tg-emoji emoji-id="5373020661574826232">👁</tg-emoji>',
    '📱': '<tg-emoji emoji-id="5834628314731387616">📱</tg-emoji>',
    '📞': '<tg-emoji emoji-id="5373020661574826232">📞</tg-emoji>',
    '🔑': '<tg-emoji emoji-id="5785167918027250397">🔑</tg-emoji>',
    '🔒': '<tg-emoji emoji-id="5785167918027250397">🔒</tg-emoji>',
    '🔓': '<tg-emoji emoji-id="5998940732545571769">🔓</tg-emoji>',
    '🛡️': '<tg-emoji emoji-id="5920298756074379058">🛡️</tg-emoji>',
    '🚫': '<tg-emoji emoji-id="5888789252493283486">🚫</tg-emoji>',
    '✅': '<tg-emoji emoji-id="6258259403200270844">✅</tg-emoji>',
    '☑️': '<tg-emoji emoji-id="4945049066271671758">☑️</tg-emoji>',
    '❌': '<tg-emoji emoji-id="5796291784539639311">❌</tg-emoji>',
    '⚠️': '<tg-emoji emoji-id="5999278377104578246">⚠️</tg-emoji>',
    '🔄': '<tg-emoji emoji-id="5976831692604709621">🔄</tg-emoji>',
    '🔙': '<tg-emoji emoji-id="5253743295141538873">🔙</tg-emoji>',
    '🆕': '<tg-emoji emoji-id="5857339990123486296">🆕</tg-emoji>',
    '🔴': '<tg-emoji emoji-id="5999278377104578246">🔴</tg-emoji>',
    '🟢': '<tg-emoji emoji-id="4945049066271671758">🟢</tg-emoji>',
    '🔵': '<tg-emoji emoji-id="5967301267549068409">🔵</tg-emoji>',
    '🔹': '<tg-emoji emoji-id="5967301267549068409">🔹</tg-emoji>',
    '🔢': '<tg-emoji emoji-id="5965466792527666087">🔢</tg-emoji>',
    '📢': '<tg-emoji emoji-id="5902385465390013835">📢</tg-emoji>',
    '📣': '<tg-emoji emoji-id="5902385465390013835">📣</tg-emoji>',
    '📡': '<tg-emoji emoji-id="5836811137370297987">📡</tg-emoji>',
    '📨': '<tg-emoji emoji-id="5920415115328362511">📨</tg-emoji>',
    '📬': '<tg-emoji emoji-id="5857339990123486296">📬</tg-emoji>',
    '📤': '<tg-emoji emoji-id="5920298756074379058">📤</tg-emoji>',
    '📥': '<tg-emoji emoji-id="5920415115328362511">📥</tg-emoji>',
    '✉️': '<tg-emoji emoji-id="5314299563761222650">✉️</tg-emoji>',
    '📊': '<tg-emoji emoji-id="5935935761336505948">📊</tg-emoji>',
    '📈': '<tg-emoji emoji-id="5935935761336505948">📈</tg-emoji>',
    '📋': '<tg-emoji emoji-id="5803363345113290876">📋</tg-emoji>',
    '📦': '<tg-emoji emoji-id="5881760620117760960">📦</tg-emoji>',
    '📂': '<tg-emoji emoji-id="5881760620117760960">📂</tg-emoji>',
    '🧾': '<tg-emoji emoji-id="5881760620117760960">🧾</tg-emoji>',
    '🗂️': '<tg-emoji emoji-id="5881760620117760960">🗂️</tg-emoji>',
    '🗑️': '<tg-emoji emoji-id="5920209833071482745">🗑️</tg-emoji>',
    '📌': '<tg-emoji emoji-id="5920298756074379058">📌</tg-emoji>',
    '🎁': '<tg-emoji emoji-id="5976317950091598658">🎁</tg-emoji>',
    '🎟️': '<tg-emoji emoji-id="5785167918027250397">🎟️</tg-emoji>',
    '🎫': '<tg-emoji emoji-id="5785167918027250397">🎫</tg-emoji>',
    '🎯': '<tg-emoji emoji-id="5965466792527666087">🎯</tg-emoji>',
    '⚙️': '<tg-emoji emoji-id="5857054220179480029">⚙️</tg-emoji>',
    '🛠️': '<tg-emoji emoji-id="5965466792527666087">🛠️</tg-emoji>',
    '➕': '<tg-emoji emoji-id="5857339990123486296">➕</tg-emoji>',
    '➖': '<tg-emoji emoji-id="5280753674451175517">➖</tg-emoji>',
    '🔍': '<tg-emoji emoji-id="5965466792527666087">🔍</tg-emoji>',
    '🔎': '<tg-emoji emoji-id="5965466792527666087">🔎</tg-emoji>',
    'ℹ️': '<tg-emoji emoji-id="5965466792527666087">ℹ️</tg-emoji>',
    '🧹': '<tg-emoji emoji-id="5920415115328362511">🧹</tg-emoji>',
    '🚀': '<tg-emoji emoji-id="5967301267549068409">🚀</tg-emoji>',
    '🔗': '<tg-emoji emoji-id="5967301267549068409">🔗</tg-emoji>',
    '⬆️': '<tg-emoji emoji-id="5920298756074379058">⬆️</tg-emoji>',
    '⬇️': '<tg-emoji emoji-id="5922681088534124293">⬇️</tg-emoji>',
    '🌐': '<tg-emoji emoji-id="5837128389424585193">🌐</tg-emoji>',
    '🌾': '<tg-emoji emoji-id="5981216003810400332">🌾</tg-emoji>',
    '📅': '<tg-emoji emoji-id="5314299563761222650">📅</tg-emoji>',
    '📝': '<tg-emoji emoji-id="5314299563761222650">📝</tg-emoji>',
    '✏️': '<tg-emoji emoji-id="5314299563761222650">✏️</tg-emoji>',
    '⏳': '<tg-emoji emoji-id="5314299563761222650">⏳</tg-emoji>',
    '⏰': '<tg-emoji emoji-id="5314299563761222650">⏰</tg-emoji>',
    '💬': '<tg-emoji emoji-id="5314299563761222650">💬</tg-emoji>',
    '🏠': '<tg-emoji emoji-id="5881760620117760960">🏠</tg-emoji>',
    '🏦': '<tg-emoji emoji-id="5803363345113290876">🏦</tg-emoji>',
    '🏷️': '<tg-emoji emoji-id="5881760620117760960">🏷️</tg-emoji>',
    '🖨️': '<tg-emoji emoji-id="5967617875358258757">🖨️</tg-emoji>',
    '🖼️': '<tg-emoji emoji-id="5294079682365384341">🖼️</tg-emoji>',
}


def ce(text):
    if not text:
        return text
    for ch, rep in _CE.items():
        text = text.replace(ch, rep)
    return text


# ═══════════════════════════════════════════════════════════
#                    أدوات مساعدة
# ═══════════════════════════════════════════════════════════
def normalize_msisdn(msisdn):
    d = re.sub(r'\D', '', str(msisdn))
    if d.startswith("964"):
        d = d[3:]
    if d.startswith("0"):
        d = d[1:]
    return d


def validate_msisdn(msisdn):
    d = normalize_msisdn(msisdn)
    return len(d) == 10 and d.startswith(("77", "78"))


def decode_jwt(token):
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return None
        pad = lambda s: s + "=" * (-len(s) % 4)
        return {
            "header": json.loads(base64.urlsafe_b64decode(pad(parts[0]))),
            "payload": json.loads(base64.urlsafe_b64decode(pad(parts[1]))),
        }
    except Exception:
        return None


def identify_token_type(token):
    d = decode_jwt(token)
    if not d:
        return "invalid"
    if d["payload"].get("data", {}).get("grant_type") == "refresh":
        return "refresh"
    return "access"


def get_msisdn_from_token(token):
    d = decode_jwt(token)
    if not d:
        return None
    return d["payload"].get("data", {}).get("msisdn")


def get_expiry_from_token(token):
    d = decode_jwt(token)
    if not d:
        return None
    return d["payload"].get("expires") or d["payload"].get("exp")


def fmt_ts(ts):
    if not ts:
        return "—"
    try:
        if isinstance(ts, str):
            try:
                return datetime.fromisoformat(ts.replace("Z", "")).strftime("%Y-%m-%d %H:%M")
            except Exception:
                ts = float(ts)
        if ts > 1e11:
            ts = ts / 1000
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return str(ts)[:19]


def days_from_now(ts_str):
    if not ts_str:
        return None
    try:
        d = datetime.fromisoformat(ts_str.replace("Z", ""))
        return (d - datetime.now()).days
    except Exception:
        return None


def api_get(path, token, **params):
    headers = {**COMMON_HEADERS, "Authorization": f"Bearer {token}"}
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=headers, params=params, timeout=15)
        if r.status_code == 200:
            return r.json()
        return {"status": "error", "code": r.status_code}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def esc(t):
    if t is None:
        return "—"
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def login_zain(msisdn, password):
    try:
        r = requests.post(
            f"{BASE_URL}/user/login",
            data=json.dumps({"msisdn": msisdn, "password": password}),
            headers=COMMON_HEADERS,
            timeout=15
        )
        data = r.json()
        if data.get("status") != "success":
            err = data.get("error", {})
            return None, err.get("message", "فشل تسجيل الدخول")
        return data["data"]["access_token"], None
    except Exception as e:
        return None, str(e)


# ═══════════════════════════════════════════════════════════
#                    جلب البيانات
# ═══════════════════════════════════════════════════════════
def fetch_all_data(token, msisdn):
    data = {}

    r = api_get("/v2/user/profile", token)
    data["profile"] = r.get("data", {}) if r.get("status") == "success" else {}

    r = api_get("/number/wallet", token, msisdn=msisdn)
    data["wallet"] = r.get("data", {}) if r.get("status") == "success" else {}

    r = api_get("/number/subaccounts", token, msisdn=msisdn)
    data["subaccounts"] = r.get("data", []) if r.get("status") == "success" else []

    r = api_get("/loyalty/info", token)
    data["loyalty"] = r.get("data", {}) if r.get("status") == "success" else {}

    r = api_get("/number/subscriptions", token, msisdn=msisdn)
    data["subscriptions"] = r.get("data", []) if r.get("status") == "success" else []

    r = api_get("/notifications", token, offset=0, limit=10)
    data["notifications"] = r.get("data", {}) if r.get("status") == "success" else {}

    return data


def get_user_data(user_id, token, msisdn, force=False):
    now = time.time()
    cached = CACHE.get(user_id)
    if not force and cached and (now - cached.get("ts", 0)) < 60:
        return cached["data"]
    data = fetch_all_data(token, msisdn)
    CACHE[user_id] = {"data": data, "ts": now}
    return data


# ═══════════════════════════════════════════════════════════
#                    تنسيق التقارير
# ═══════════════════════════════════════════════════════════
ACCOUNT_TYPE_NAMES = {
    1000: "💵 رصيد أساسي",
    1001: "🎁 رصيد مكافآت",
    2000: "💰 رصيد مالي",
    2001: "📶 رصيد بيانات",
    2784: "📞 دقائق",
    4425: "🎁 رصيد مجاني",
    4426: "💬 رسائل",
    4427: "🌐 إنترنت",
    6083: "🎯 رصيد إضافي",
}

STATUS_NAMES = {
    "Active":    "🟢 نشط",
    "Renewing":  "🔄 قيد التجديد",
    "Expiring":  "🟡 قارب على الانتهاء",
    "Expired":   "🔴 منتهي",
    "Suspended": "⚫ موقوف",
    "Pending":   "🔵 قيد التفعيل",
}


def fmt_summary(data, msisdn):
    p = data.get("profile", {})
    w = data.get("wallet", {})
    l = data.get("loyalty", {})
    subs = data.get("subscriptions", [])

    name = p.get("name", "—")
    balance = w.get("balance", {}).get("value", 0)
    points = l.get("total_points", 0)
    tier_ar = l.get("localized_tier", {}).get("ar", "—")

    return (
        f"📱 【 الرقم 】  <code>{esc(msisdn)}</code>\n"
        f"👤 【 الاسم 】  <b>{esc(name)}</b>\n"
        f"💰 【 الرصيد 】  <b>{balance} د.ع</b>\n"
        f"🏆 【 نقاط ممنون 】  <b>{points:,}</b>\n"
        f"⭐ 【 المستوى 】  <b>{esc(tier_ar)}</b>\n"
        f"📦 【 الاشتراكات 】  <b>{len(subs)}</b>\n"
    )


def fmt_profile(data):
    p = data.get("profile", {})
    if not p:
        return "🔴 تعذّر جلب الملف الشخصي"

    billing_ar = {
        "prepaid_normal": "دفع مسبق عادي",
        "postpaid": "دفع لاحق",
        "hybrid": "مختلط",
    }.get(p.get("customer_billing_type", ""), p.get("customer_billing_type", "—"))

    flex_ar = {
        "eligible": "✅ مؤهل",
        "migrated": "🔄 تم الترحيل",
        "not_eligible": "❌ غير مؤهل",
    }.get(p.get("flex_status", ""), p.get("flex_status", "—"))

    return (
        f"<b>👤  【 الملف الشخصي 】</b>\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"👋 【 الاسم 】 {esc(p.get('name'))}\n"
        f"📱 【 الرقم 】 <code>{esc(p.get('msisdn'))}</code>\n"
        f"📅 【 التسجيل 】 {esc(fmt_ts(p.get('created_at')))}\n"
        f"💳 【 نوع الحساب 】 {esc(billing_ar)}\n"
        f"📶 【 الشريحة 】 {esc(p.get('unified_sim_status'))}\n"
        f"🌐 【 4G 】 {'✅ نعم' if p.get('is_4g_compatible') else '❌ لا'}\n"
        f"🎁 【 كفو 】 {'✅ مستلم' if p.get('is_gift_redeemed') else '❌ لم يُستلم'}\n"
        f"⚡ 【 Flex 】 {esc(flex_ar)}\n"
        f"🎫 【 الباقة 】 <code>#{esc(p.get('primary_offering_id', '—'))}</code>\n"
    )


def fmt_balance(data):
    w = data.get("wallet", {})
    bal = w.get("balance", {})
    amount = bal.get("value", 0)
    expiry = bal.get("expiry", "")

    txt = (
        f"<b>💰  【 الرصيد المالي 】</b>\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"💵 【 الرصيد 】 <b>{amount} دينار</b>\n"
    )

    if expiry:
        txt += f"📅 【 صالح لغاية 】 {esc(expiry[:10])}\n"
        days = days_from_now(expiry)
        if days is not None and days > 0:
            txt += f"⏳ 【 المتبقي 】 <b>{days} يوم</b>\n"

    if w.get("loan"):
        txt += f"💸 【 سلفة 】 {esc(str(w.get('loan')))}\n"

    subs = data.get("subaccounts", [])
    if subs:
        txt += "\n📊 【 تفصيل الرصيد 】\n"
        for s in subs:
            label = ACCOUNT_TYPE_NAMES.get(s.get("account_type"), f"نوع #{s.get('account_type')}")
            amt = s.get("amount", 0)
            line = f"  • {label}: <b>{amt:,}</b>"
            exp = s.get("expiry_date", "")
            if exp and exp != "2037-01-01T00:00:00":
                days = days_from_now(exp)
                if days is not None:
                    line += f" <i>({days} يوم)</i>"
            txt += line + "\n"

    return txt


def fmt_loyalty(data):
    l = data.get("loyalty", {})
    if not l:
        return "🔴 تعذّر جلب نقاط ممنون"

    tier_ar = l.get("localized_tier", {}).get("ar", l.get("tier", "—"))
    next_ar = l.get("localized_next_tier", {}).get("ar", l.get("next_tier", "—"))

    total = l.get("total_points", 0)
    spendable = l.get("total_spendable_points", 0)
    to_next = l.get("points_to_next_tier", 0)
    total_next = l.get("total_points_to_next_tier", 0)
    earned = total_next - to_next

    pct = (earned / total_next * 100) if total_next else 0
    filled = int(20 * pct / 100)
    bar = "█" * filled + "░" * (20 - filled)

    txt = (
        f"<b>🏆  【 نقاط ممنون 】</b>\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"⭐ 【 المستوى الحالي 】 <b>{esc(tier_ar)}</b>\n"
        f"🥇 【 المستوى التالي 】 <b>{esc(next_ar)}</b>\n"
        f"📅 【 الانضمام 】 {esc(fmt_ts(l.get('tenure')))}\n"
        f"\n"
        f"💎 【 مجموع النقاط 】 <b>{total:,}</b>\n"
        f"💰 【 نقاط للاستبدال 】 <b>{spendable:,}</b>\n"
        f"📈 【 للترقية 】 <b>{to_next} نقطة</b>\n"
        f"\n"
        f"📊 【 التقدم 】\n"
        f"<code>[{bar}] {pct:.1f}%</code>\n"
        f"<code>{earned:,} / {total_next:,}</code>\n"
    )

    spendable_list = l.get("spendable_points", [])
    if spendable_list:
        txt += "\n🎁 【 نقاط قابلة للاستبدال 】\n"
        for p in spendable_list:
            txt += f"  • <b>{p.get('amount', 0):,}</b> نقطة <i>({p.get('validity', '')[:10]})</i>\n"

    return txt


def fmt_subs(data):
    subs = data.get("subscriptions", [])
    if not subs:
        return "<b>📦  【 الاشتراكات 】</b>\n━━━━━━━━━━━━━━━━━━━\n📭 لا توجد اشتراكات"

    txt = f"<b>📦  【 الاشتراكات ({len(subs)}) 】</b>\n━━━━━━━━━━━━━━━━━━━\n"

    for i, s in enumerate(subs, 1):
        status_str = STATUS_NAMES.get(s.get("status"), s.get("status", "—"))
        txt += (
            f"\n<b>#{i}</b> <code>{s.get('id')}</code>\n"
            f"  🔵 【 الحالة 】 {esc(status_str)}\n"
            f"  📅 【 التفعيل 】 {esc(fmt_ts(s.get('effective_time')))}\n"
            f"  📅 【 الانتهاء 】 {esc(fmt_ts(s.get('expire_time')))}\n"
        )
        days = days_from_now(s.get("expire_time"))
        if days is not None:
            txt += f"  ⏳ 【 المتبقي 】 <b>{days} يوم</b>\n"
        if s.get("is_kafoo_offer"):
            txt += "  👑 【 عرض كفو 】\n"

    return txt


def fmt_notifs(data):
    n = data.get("notifications", {})
    total = n.get("total_count", 0)
    unread = n.get("unread_count", 0)
    notifs = n.get("notifications", [])

    txt = (
        f"<b>📬  【 الإشعارات 】</b>\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"📊 【 الإجمالي 】 {total}\n"
        f"🔵 【 غير مقروء 】 {unread}\n"
    )

    if notifs:
        txt += "\n<b>آخر الإشعارات:</b>\n"
        for notif in notifs[:5]:
            icon = "🔵" if not notif.get("is_read") else "⚪"
            txt += f"  {icon} {esc(fmt_ts(notif.get('date_time')))}\n"

    return txt


def fmt_token_info(state):
    token = state.get("token", "")
    exp = get_expiry_from_token(token)
    hours = max(0, (exp - time.time()) / 3600) if exp else 0

    return (
        f"<b>🔑  【 معلومات التوكن 】</b>\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"📱 【 الحساب 】 <code>{esc(state.get('msisdn'))}</code>\n"
        f"📅 【 ينتهي 】 {esc(fmt_ts(exp))}\n"
        f"⏳ 【 المتبقي 】 <b>{hours:.1f} ساعة</b>\n"
        f"📏 【 الطول 】 {len(token)} حرف\n"
    )


# ═══════════════════════════════════════════════════════════
#                    الأزرار (telebot)
# ═══════════════════════════════════════════════════════════
def kb_main(msisdn="—"):
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_account = types.InlineKeyboardButton(f"👑 الحساب: {msisdn} 👑", callback_data="noop")
    btn_profile = types.InlineKeyboardButton("👤 الملف", callback_data="profile")
    btn_balance = types.InlineKeyboardButton("💰 الرصيد", callback_data="balance")
    btn_loyalty = types.InlineKeyboardButton("🏆 نقاط ممنون", callback_data="loyalty")
    btn_subs = types.InlineKeyboardButton("📦 الاشتراكات", callback_data="subs")
    btn_notifs = types.InlineKeyboardButton("📬 الإشعارات", callback_data="notifs")
    btn_token = types.InlineKeyboardButton("🔑 التوكن", callback_data="token_info")
    btn_report = types.InlineKeyboardButton("📋 تقرير شامل", callback_data="full_report")
    btn_refresh = types.InlineKeyboardButton("🔄 تحديث", callback_data="refresh")
    btn_logout = types.InlineKeyboardButton("🚪 خروج", callback_data="logout")
    btn_info = types.InlineKeyboardButton("ℹ️ معلومات البوت", callback_data="bot_info")
    btn_dev = types.InlineKeyboardButton("👨‍💻 المطور", url=DEV_LINK)
    btn_channel = types.InlineKeyboardButton("📢 القناة", url=CHANNEL_LINK)

    markup.row(btn_account)
    markup.row(btn_profile, btn_balance)
    markup.row(btn_loyalty, btn_subs)
    markup.row(btn_notifs, btn_token)
    markup.row(btn_report)
    markup.row(btn_refresh, btn_logout)
    markup.row(btn_info)
    markup.row(btn_dev, btn_channel)

    return markup


def kb_back():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_back = types.InlineKeyboardButton("🔙 رجوع", callback_data="menu")
    btn_refresh = types.InlineKeyboardButton("🔄 تحديث", callback_data="refresh_section")
    btn_home = types.InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="menu")

    markup.row(btn_back, btn_refresh)
    markup.row(btn_home)

    return markup


# ═══════════════════════════════════════════════════════════
#                    أوامر البوت
# ═══════════════════════════════════════════════════════════
@bot.message_handler(commands=["start"])
def cmd_start(message):
    user = message.from_user
    USER_STATE[user.id] = {"step": "waiting_input", "name": user.first_name}

    welcome = (
        f"👑 <b>أهلاً {esc(user.first_name)}</b>\n\n"
        f"✨ <b>بوت زين العراق</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🔵 <b>كيفية الاستخدام:</b>\n\n"
        f"📱 <b>الطريقة 1 — رقم + كلمة مرور:</b>\n"
        f"  أرسل رقمك مباشرة\n"
        f"  مثال: <code>7801234567</code>\n\n"
        f"🔑 <b>الطريقة 2 — access_token:</b>\n"
        f"  أرسل التوكن مباشرة\n"
        f"  البوت سيتعرف عليه تلقائياً\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🛡️ <b>حقوق التطوير:</b> {DEVELOPER}\n"
    )

    bot.send_message(message.chat.id, ce(welcome), parse_mode="HTML")


@bot.message_handler(commands=["menu"])
def cmd_menu(message):
    user_id = message.from_user.id
    state = USER_STATE.get(user_id, {})

    if not state.get("token"):
        bot.send_message(message.chat.id, ce("🔴 لا يوجد حساب مسجل. ابدأ بـ /start"), parse_mode="HTML")
        return

    text = (
        f"🏠 <b>القائمة الرئيسية</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📱 الحساب: <code>{esc(state.get('msisdn'))}</code>"
    )
    bot.send_message(message.chat.id, ce(text), parse_mode="HTML",
                     reply_markup=kb_main(state.get("msisdn")))


@bot.message_handler(commands=["dev"])
def cmd_dev(message):
    text = (
        f"🛡️ <b>حقوق التطوير</b>\n\n"
        f"✨ المطوّر: {DEVELOPER}\n"
        f"🔥 الرابط: {DEV_LINK}"
    )
    bot.send_message(message.chat.id, ce(text), parse_mode="HTML")


# ═══════════════════════════════════════════════════════════
#                    معالجة الرسائل
# ═══════════════════════════════════════════════════════════
@bot.message_handler(content_types=["text"])
def handle_message(message):
    user_id = message.from_user.id
    text = message.text.strip()

    if not text:
        return

    state = USER_STATE.get(user_id, {})

    # ─── 1. كلمة المرور ───
    if state.get("step") == "waiting_password":
        msisdn = state["msisdn"]
        password = text

        msg = bot.send_message(message.chat.id, ce("🔄 <i>جاري تسجيل الدخول...</i>"), parse_mode="HTML")

        token, error = login_zain(msisdn, password)

        if error:
            bot.edit_message_text(
                ce(f"🔴 <b>فشل تسجيل الدخول</b>\n\nالسبب: {esc(error)}\n\nحاول مرة أخرى أو اكتب /start"),
                message.chat.id, msg.message_id, parse_mode="HTML"
            )
            USER_STATE[user_id] = {"step": "waiting_input"}
            return

        try:
            bot.delete_message(message.chat.id, message.message_id)
        except Exception:
            pass

        USER_STATE[user_id] = {
            "step": "logged_in",
            "token": token,
            "msisdn": msisdn,
            "name": state.get("name", ""),
        }

        bot.edit_message_text(ce("🔄 <i>جاري جلب البيانات...</i>"),
                              message.chat.id, msg.message_id, parse_mode="HTML")
        data = get_user_data(user_id, token, msisdn, force=True)
        summary = fmt_summary(data, msisdn)

        try:
            bot.delete_message(message.chat.id, msg.message_id)
        except Exception:
            pass

        welcome_text = (
            f"🟢 <b>تم تسجيل الدخول بنجاح</b>\n\n"
            f"✨ <b>الملخص السريع</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{summary}\n"
            f"✨ <b>اختر من القائمة:</b>"
        )
        bot.send_message(message.chat.id, ce(welcome_text), parse_mode="HTML",
                         reply_markup=kb_main(msisdn))
        return

    # ─── 2. JWT token ───
    if text.startswith("eyJ") and text.count(".") == 2:
        token_type = identify_token_type(text)

        if token_type == "refresh":
            bot.send_message(
                message.chat.id,
                ce(f"⚠️ <b>هذا refresh_token وليس access_token</b>\n\n"
                   f"refresh_token لا يعمل مع الـ endpoints.\n"
                   f"استخدم access_token بدلاً منه.\n\n"
                   f"🔵 سجّل دخول برقم + كلمة مرور للحصول على access_token."),
                parse_mode="HTML"
            )
            return

        if token_type == "invalid":
            bot.send_message(message.chat.id, ce("🔴 التوكن غير صالح"), parse_mode="HTML")
            return

        msisdn = get_msisdn_from_token(text)
        exp = get_expiry_from_token(text)

        if exp and time.time() >= exp:
            bot.send_message(
                message.chat.id,
                ce(f"🔴 <b>التوكن منتهي الصلاحية</b>\n\nانتهى في: {esc(fmt_ts(exp))}"),
                parse_mode="HTML"
            )
            return

        USER_STATE[user_id] = {
            "step": "logged_in",
            "token": text,
            "msisdn": msisdn,
        }

        msg = bot.send_message(message.chat.id, ce("🔄 <i>جاري جلب البيانات...</i>"), parse_mode="HTML")
        data = get_user_data(user_id, text, msisdn, force=True)
        summary = fmt_summary(data, msisdn)

        hours = max(0, (exp - time.time()) / 3600) if exp else 0

        try:
            bot.delete_message(message.chat.id, msg.message_id)
        except Exception:
            pass

        welcome_text = (
            f"🟢 <b>تم التعرف على التوكن</b>\n\n"
            f"✨ <b>الملخص السريع</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{summary}\n"
            f"⏳ <b>صلاحية التوكن:</b> {hours:.1f} ساعة\n\n"
            f"✨ <b>اختر من القائمة:</b>"
        )
        bot.send_message(message.chat.id, ce(welcome_text), parse_mode="HTML",
                         reply_markup=kb_main(msisdn))
        return

    # ─── 3. رقم ───
    if re.match(r'^[+]?[\d\s\-]{9,}$', text):
        msisdn = normalize_msisdn(text)

        if not validate_msisdn(msisdn):
            bot.send_message(
                message.chat.id,
                ce("🔴 <b>رقم غير صالح</b>\n\nيجب أن يبدأ بـ 077 أو 078 ويتكون من 10 أرقام"),
                parse_mode="HTML"
            )
            return

        USER_STATE[user_id] = {
            "step": "waiting_password",
            "msisdn": msisdn,
            "name": state.get("name", ""),
        }

        bot.send_message(
            message.chat.id,
            ce(f"📱 <b>الرقم:</b> <code>{esc(msisdn)}</code>\n\n"
               f"🔑 <b>أرسل كلمة المرور الآن</b>\n"
               f"<i>(سيتم حذف رسالة كلمة المرور تلقائياً للأمان)</i>"),
            parse_mode="HTML"
        )
        return

    # ─── 4. غير معروف ───
    bot.send_message(
        message.chat.id,
        ce(f"⚠️ <b>لم أفهم المدخل</b>\n\n"
           f"أرسل:\n"
           f"  📱 رقم الهاتف (مثل: 07801234567)\n"
           f"  🔑 أو access_token"),
        parse_mode="HTML"
    )


# ═══════════════════════════════════════════════════════════
#                    معالجة الأزرار
# ═══════════════════════════════════════════════════════════
@bot.callback_query_handler(func=lambda call: True)
def button_callback(call):
    query = call
    user_id = query.from_user.id
    state = USER_STATE.get(user_id, {})
    action = query.data

    if action == "noop":
        bot.answer_callback_query(query.id, "")
        return

    # ─── معلومات البوت ───
    if action == "bot_info":
        text = (
            f"ℹ️ <b>معلومات البوت</b>\n"
            f"━━━━━━━━━━━━━━━━━━━\n\n"
            f"👑 <b>الاسم:</b> بوت زين العراق\n"
            f"📌 <b>الوصف:</b> واجهة تفاعلية لحساب زين\n"
            f"🔖 <b>الإصدار:</b> v8.0 (Telebot)\n"
            f"👨‍💻 <b>المطور:</b> {DEVELOPER}\n"
            f"📢 <b>القناة:</b> {CHANNEL_LINK}\n"
            f"━━━━━━━━━━━━━━━━━━━\n\n"
            f"✨ <b>المميزات:</b>\n"
            f"  • عرض الرصيد الكامل\n"
            f"  • نقاط ممنون والمستوى\n"
            f"  • الاشتراكات والإشعارات\n"
            f"  • تقرير شامل\n"
            f"  • إيموجيات مميزة 🎨\n"
            f"━━━━━━━━━━━━━━━━━━━"
        )
        try:
            bot.edit_message_text(
                ce(text),
                query.message.chat.id,
                query.message.message_id,
                parse_mode="HTML",
                reply_markup=kb_back()
            )
        except Exception:
            bot.send_message(query.message.chat.id, ce(text), parse_mode="HTML", reply_markup=kb_back())
        bot.answer_callback_query(query.id, "")
        return

    if action not in ("menu",) and not state.get("token"):
        bot.answer_callback_query(query.id, "جلسة منتهية. ابدأ بـ /start", show_alert=True)
        return

    token = state.get("token")
    msisdn = state.get("msisdn")

    # ─── رجوع للقائمة ───
    if action == "menu":
        data = get_user_data(user_id, token, msisdn)
        summary = fmt_summary(data, msisdn)
        text = (
            f"🏠 <b>القائمة الرئيسية</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"✨ <b>الملخص السريع</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{summary}"
        )
        try:
            bot.edit_message_text(
                ce(text),
                query.message.chat.id,
                query.message.message_id,
                parse_mode="HTML",
                reply_markup=kb_main(msisdn)
            )
        except Exception:
            bot.send_message(query.message.chat.id, ce(text), parse_mode="HTML", reply_markup=kb_main(msisdn))
        bot.answer_callback_query(query.id, "")
        return

    # ─── تحديث ───
    if action in ("refresh", "refresh_section"):
        CACHE.pop(user_id, None)
        data = get_user_data(user_id, token, msisdn, force=True)
        summary = fmt_summary(data, msisdn)
        text = (
            f"🔄 <b>تم التحديث</b>\n\n"
            f"✨ <b>الملخص السريع</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{summary}"
        )
        try:
            bot.edit_message_text(
                ce(text),
                query.message.chat.id,
                query.message.message_id,
                parse_mode="HTML",
                reply_markup=kb_main(msisdn)
            )
        except Exception:
            bot.send_message(query.message.chat.id, ce(text), parse_mode="HTML", reply_markup=kb_main(msisdn))
        bot.answer_callback_query(query.id, "✅ تم التحديث")
        return

    # ─── خروج ───
    if action == "logout":
        USER_STATE.pop(user_id, None)
        CACHE.pop(user_id, None)
        try:
            bot.edit_message_text(
                ce("🚪 <b>تم تسجيل الخروج بنجاح</b>\n\nللدخول مجدداً، أرسل /start"),
                query.message.chat.id,
                query.message.message_id,
                parse_mode="HTML"
            )
        except Exception:
            bot.send_message(query.message.chat.id, ce("🚪 <b>تم تسجيل الخروج بنجاح</b>"), parse_mode="HTML")
        bot.answer_callback_query(query.id, "")
        return

    # ─── جلب البيانات ───
    data = get_user_data(user_id, token, msisdn)

    # ─── الملف الشخصي ───
    if action == "profile":
        text = fmt_profile(data)
        try:
            bot.edit_message_text(ce(text), query.message.chat.id, query.message.message_id,
                                  parse_mode="HTML", reply_markup=kb_back())
        except Exception:
            bot.send_message(query.message.chat.id, ce(text), parse_mode="HTML", reply_markup=kb_back())
        bot.answer_callback_query(query.id, "")
        return

    # ─── الرصيد ───
    if action == "balance":
        text = fmt_balance(data)
        try:
            bot.edit_message_text(ce(text), query.message.chat.id, query.message.message_id,
                                  parse_mode="HTML", reply_markup=kb_back())
        except Exception:
            bot.send_message(query.message.chat.id, ce(text), parse_mode="HTML", reply_markup=kb_back())
        bot.answer_callback_query(query.id, "")
        return

    # ─── نقاط ممنون ───
    if action == "loyalty":
        text = fmt_loyalty(data)
        try:
            bot.edit_message_text(ce(text), query.message.chat.id, query.message.message_id,
                                  parse_mode="HTML", reply_markup=kb_back())
        except Exception:
            bot.send_message(query.message.chat.id, ce(text), parse_mode="HTML", reply_markup=kb_back())
        bot.answer_callback_query(query.id, "")
        return

    # ─── الاشتراكات ───
    if action == "subs":
        text = fmt_subs(data)
        try:
            bot.edit_message_text(ce(text), query.message.chat.id, query.message.message_id,
                                  parse_mode="HTML", reply_markup=kb_back())
        except Exception:
            bot.send_message(query.message.chat.id, ce(text), parse_mode="HTML", reply_markup=kb_back())
        bot.answer_callback_query(query.id, "")
        return

    # ─── الإشعارات ───
    if action == "notifs":
        text = fmt_notifs(data)
        try:
            bot.edit_message_text(ce(text), query.message.chat.id, query.message.message_id,
                                  parse_mode="HTML", reply_markup=kb_back())
        except Exception:
            bot.send_message(query.message.chat.id, ce(text), parse_mode="HTML", reply_markup=kb_back())
        bot.answer_callback_query(query.id, "")
        return

    # ─── التوكن ───
    if action == "token_info":
        text = fmt_token_info(state)
        try:
            bot.edit_message_text(ce(text), query.message.chat.id, query.message.message_id,
                                  parse_mode="HTML", reply_markup=kb_back())
        except Exception:
            bot.send_message(query.message.chat.id, ce(text), parse_mode="HTML", reply_markup=kb_back())
        bot.answer_callback_query(query.id, "")
        return

    # ─── تقرير شامل ───
    if action == "full_report":
        txt = (
            f"📋 <b>التقرير الشامل</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{fmt_summary(data, msisdn)}\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{fmt_profile(data)}\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{fmt_balance(data)}\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{fmt_loyalty(data)}\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{fmt_subs(data)}\n"
        )

        if len(txt) > 4000:
            try:
                bot.edit_message_text(ce(fmt_summary(data, msisdn)),
                                      query.message.chat.id, query.message.message_id,
                                      parse_mode="HTML", reply_markup=kb_back())
            except Exception:
                pass
            for section_txt in [fmt_profile(data), fmt_balance(data), fmt_loyalty(data), fmt_subs(data)]:
                bot.send_message(query.message.chat.id, ce(section_txt), parse_mode="HTML")
        else:
            try:
                bot.edit_message_text(ce(txt), query.message.chat.id, query.message.message_id,
                                      parse_mode="HTML", reply_markup=kb_back())
            except Exception:
                bot.send_message(query.message.chat.id, ce(txt), parse_mode="HTML", reply_markup=kb_back())
        bot.answer_callback_query(query.id, "")
        return


# ═══════════════════════════════════════════════════════════
#                    التشغيل
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("🔥 جاري تشغيل البوت...")
    print(f"🔑 Token: {BOT_TOKEN[:15]}...")
    print(f"👨‍💻 Developer: {DEVELOPER}")
    print(f"🟢 البوت يعمل — المطوّر: {DEVELOPER}")

    bot.infinity_polling(timeout=30, long_polling_timeout=30)
