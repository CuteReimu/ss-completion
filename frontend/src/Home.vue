<template>
  <el-alert title="感谢计时器生成器交流群的群友们热心提供存档，协助开发。代码仓库：https://github.com/CuteReimu/ss-completion" type="info" effect="dark" close-text="前往" @close="openGithub"></el-alert>
  <el-tabs v-model="currentGame" @tab-change="onChangeTab">
    <el-tab-pane label="空洞骑士" name="hollow" />
    <el-tab-pane label="丝之歌" name="silksong" />
  </el-tabs>
  <div class="btn-container">
    <el-button @click="refreshUserDataFiles" type="primary">刷新列表</el-button>
    <el-select
      v-model="selectedUserDataFile"
      :options="userDataFiles"
      style="max-width: 220px"
      placeholder="选择本地存档"
      @change="selectUserData"
    ></el-select>
    <el-button
      type="primary"
      @click="refreshUserDataFile"
      :disabled="disableReloadBtn"
    ><el-icon><RefreshRight /></el-icon></el-button>
    <el-button @click="OpenDataFolder" type="primary" style="margin-right: 15px">打开存档目录</el-button>
    <el-button @click="onChooseDataFile" type="primary">手动选择存档</el-button>
    <el-button @click="outputResult" type="danger" :disabled="disableReloadBtn">导出解析后的存档</el-button>
    <el-button @click="modifyAnalyzeScript" type="danger">修改解析脚本</el-button>
    <el-button @click="captureApp" type="primary" :disabled="isCapturing" :loading="isCapturing">截图</el-button>
    <el-switch v-model="isSortedByScene" inline-prompt active-text="按区域排序" inactive-text="按分类排序" style="margin-left:10px" size="large"></el-switch>
  </div>
  <el-text size="large" style="margin: 10px 0;">完成度：{{data.Completion ?? 0}}%{{data.PlayTime ? "&emsp;游戏时长：" + data.PlayTime : ""}}</el-text>
  <div class="card-container">
    <el-card v-for="category in (isSortedByScene?resultByScene:data.Categories)">
      <template #header>{{category.name}}</template>
      <el-table :show-header="false" border :data="category.items" :row-class-name="determineRowClass" @row-click="goToWiki">
        <el-table-column label="名称">
          <template #default="scope">
            <el-tooltip effect="dark" v-if="scope.row.desc" :content="scope.row.desc" placement="left">
              <div><el-image v-if="scope.row.icon" :src="scope.row.icon" fit="scale-down" />{{scope.row.show_text}}</div>
            </el-tooltip>
            <div v-else><el-image v-if="scope.row.icon" :src="scope.row.icon" fit="scale-down" />{{scope.row.show_text}}</div>
          </template>
        </el-table-column>
        <el-table-column prop="status_text" label="状态" width="80">
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import {ref, onMounted, computed} from 'vue';
import {
  ElAlert, ElText, ElIcon, ElTable, ElTableColumn, ElTabs, ElTabPane,
  ElButton, ElMessage, ElCard, ElTooltip, ElImage, ElSelect, ElSwitch,
} from 'element-plus';
import { RefreshRight } from '@element-plus/icons-vue';
import { BrowserOpenURL, LogError } from '../wailsjs/runtime';
import {
  OpenDataFolder, ChooseDataFile, SaveBuf, ModifyScript, SaveScreenshot,
  ShowDataFolder, SelectUserData, ChangeGame, RefreshUserData,
} from '../wailsjs/go/main/App';
import { main } from "../wailsjs/go/models";
import html2canvas from 'html2canvas';
import { sortResultByScene } from './utils';

interface OptionData {
  label: string
  value: string
}

const disableReloadBtn = ref(true);
const data = ref<main.AnalyzeResult>(new main.AnalyzeResult());
const selectedUserDataFile = ref("");
const userDataFiles = ref<OptionData[]>([]);
const currentGame = ref("silksong");
const isCapturing = ref(false);
const isSortedByScene = ref(false);
const resultByScene = computed(() => sortResultByScene(data.value));

const refreshUserDataFiles = () => {
  ShowDataFolder().then(files => {
    userDataFiles.value = files;
  });
};

const refreshUserDataFile = () => {
  RefreshUserData().then(res => {
    data.value = res;
    ElMessage({ message: "解析成功", type: 'success', plain: true });
  }).catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  });
};

const selectUserData = () => {
  SelectUserData(selectedUserDataFile.value).then(res => {
    data.value = res;
    ElMessage({ message: "解析成功", type: 'success', plain: true });
  }).catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  }).finally(() => {
    disableReloadBtn.value = false;
  });
};

const onChangeTab = gameName => {
  ChangeGame(gameName).then(() => {
    disableReloadBtn.value = true;
    selectedUserDataFile.value = "";
    data.value = new main.AnalyzeResult();
    refreshUserDataFiles();
  });
};

const determineRowClass = ({row}) => {
  let c = '';
  switch (row.status) {
    case 2: c = 'success-row'; break;
    case 1: c = 'warning-row'; break;
    default: c = 'danger-row'; break;
  }
  if (row.wiki) c += " clickable-row";
  return c;
};

const onChooseDataFile = () => {
  ChooseDataFile().then(res => {
    if (!res) return;
    data.value = res;
    ElMessage({ message: "解析成功", type: 'success', plain: true });
  }).catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  }).finally(() => {
    disableReloadBtn.value = false;
  });
};

const outputResult = () => {
  SaveBuf().catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  })
};

const modifyAnalyzeScript = () => {
  ModifyScript().catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  })
};

const openGithub = () => {
  BrowserOpenURL('https://github.com/CuteReimu/ss-completion');
};

const goToWiki = (row: main.ItemResult) => {
  if (row.wiki) BrowserOpenURL(row.wiki);
};

onMounted(() => {
  refreshUserDataFiles();
});

const captureApp = () => {
  isCapturing.value = true;
  html2canvas(document.body, {
    useCORS: true,
    scale: 1,
  }).then(canvas => {
    SaveScreenshot(canvas.toDataURL('image/png')).then(() => {
      ElMessage({ message: "截图已保存到剪贴板", type: 'success', plain: true });
    }).catch(e => {
      console.log(e);
      ElMessage({ message: String(e), type: 'error', plain: true });
    });
  }).catch(err => {
    console.log(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  }).finally(() => {
    isCapturing.value = false;
  });
};
</script>
