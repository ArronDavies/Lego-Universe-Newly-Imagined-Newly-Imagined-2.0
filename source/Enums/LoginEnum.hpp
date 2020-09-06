#pragma once

#include <memory>

namespace Garmadon {
	enum class LoginEnum : uint8_t {
		COULDNT_SIGN_IN = 0x00,
		SUCCESS = 0x01,
		ACCOUNT_IS_BANNED = 0x02,
		ACCOUNT_PERMISSIONS_NOT_HIGH_ENOUGH = 0x05,
		INVALID_PASSWORD = 0x06,
		INVALID_USERNAME = 0x08,
		ACCOUNT_ACTIVATION_PENDING = 0x09,
		ACCOUNT_IS_DISABLED = 0x0a,
		GAME_TIME_EXPIRED = 0x0b,
		FREE_TRIAL_HAS_ENDED = 0x0c,
		PLAY_SCHEDULE_NOT_ALLOWED = 0x0d,
		ACCOUNT_NOT_ACTIVATED = 0x0e
	};
}